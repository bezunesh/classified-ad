from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from ad.models import Category, Post
from ad.forms import SignupForm, PostForm

def create_category(name, description):
    return Category.objects.create(name=name, description=description)

def create_post(title, address, description, email, phone, category, published_date, author):
    return Post.objects.create(
        title=title,
        description=description,
        address=address,
        email=email,
        phone=phone,
        category=category,
        published_date=published_date,
        author=author
    )
def create_user(fname, lname, username, password, email):
    return User.objects.create_user(username, email=email, password=password,
    first_name=fname, last_name=lname)

class ViewTestCase(TestCase):
    def setUp(self):
        user1 = create_user('Bezu', 'Alemu', 'bezu', '123bezuT!', 'bezu@example.com')
        category1 = create_category('Babysitting', 'Babysitting')
        create_post('I need a baby sitter', 'Baby sitter needed', '123 street Alexandria, VA',
            'myemail@example.com','89089898',category1, timezone.now(), user1)

        create_category('For Rent', 'For Rent')
    def test_index_with_no_category(self):
        '''
        index view returns an empty category context if there are no categories
        '''
        Category.objects.all().delete()
        response = self.client.get(reverse('ad:index'))
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.context['cat_posts'], {})
        self.assertQuerysetEqual(response.context['nav_categories'], [])
    
    def test_index_with_one_category_no_post(self):
        '''
        index view stores a category in a template context
        '''
        category1 = Category.objects.get(name='Babysitting')
        category1.post_set.all().delete()
        response = self.client.get(reverse('ad:index'))
        context = response.context['cat_posts']
        self.assertIn(category1, context)
        self.assertQuerysetEqual(context[category1], [])
    
    def test_index_with_category_post(self):
        category1 = Category.objects.get(name='Babysitting')
        response = self.client.get(reverse('ad:index')) 
        data = response.context['cat_posts']   
        self.assertQuerysetEqual(data[category1], ['<Post: I need a baby sitter>'])

    def test_category(self):
        '''
        category view fetches a category by id and assigns it
        to the the context variable
        '''
        category1 = Category.objects.get(name='Babysitting')
        response = self.client.get(reverse('ad:category', args=[category1.id ]))
        self.assertEqual(response.context['category'], category1)

    def test_profile(self):
        '''
        profile view lists posts of the current user
        '''
        self.client.login(username='bezu', password='123bezuT!')
        user1 = User.objects.get(username='bezu')
        response = self.client.get(reverse('ad:profile', args=[user1.id]))
        self.assertQuerysetEqual(response.context['posts'], ['<Post: I need a baby sitter>'])

    def test_signup_getrequest(self):
        '''
        sign up view shows a signup form when a GET request is issued
        '''
        response = self.client.get(reverse('ad:signup'))
        self.assertIsInstance(response.context['form'], SignupForm)
        
    def test_signup_postrequest(self):
        '''
        signup post request creates a new user account 
        if submited form data is valid  and redirecs to login view
        '''
        data = {'username': 'bezunesh', 'password': '12345678', 
         'first_name': 'bezu', 'last_name': 'alemu', 'email': 'xx@example.com'}
        response = self.client.post(reverse('ad:signup'), data)
        user1 = User.objects.filter(username='bezunesh')
        self.assertQuerysetEqual(user1, ['<User: bezunesh>'])
        self.assertEqual(response.status_code, HttpResponseRedirect.status_code)
    
    def test_user_posts(self):
        '''
        userPosts view lists a given user's posts
        '''
        user1 = User.objects.get(username='bezu')
        response = self.client.get(reverse('ad:user_posts', args=[user1.id]))
        self.assertQuerysetEqual(response.context['posts'], ['<Post: I need a baby sitter>'])

    def test_create_ad_annonymous_user(self):
        ''' 
        createAd view redirects a user to login page if user is not logged in
        ''' 
        response = self.client.get(reverse('ad:create-ad'))
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.status_code, HttpResponseRedirect.status_code)
    
    def test_create_ad_loggedin_user(self):
        '''
        createAd view renders a PostForm for a loggedin user
        '''
        self.client.login(username='bezu', password='123bezuT!')
        response = self.client.get(reverse('ad:create-ad'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], PostForm)

    def test_create_ad_post_ad(self):
        '''
        createAd allows a logged in user to create a new post
        '''
        self.client.login(username='bezu', password='123bezuT!')
        category = Category.objects.get(name='For Rent')
        data = {
            'title':'A house for rent',
            'address': '123 street',
            'description': 'A house for rent in a nice location',
            'phone':'7039876789',
            'category': category.id,
            'author': User.objects.get(username='bezu').id,
            'email': 'bezu@example.com'
        }
        response = self.client.post(reverse('ad:create-ad'), data)
        latest_post = Post.objects.latest('id')
        self.assertIsInstance(latest_post, Post)
        self.assertEqual(latest_post.title, 'A house for rent')
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.status_code, HttpResponseRedirect.status_code)
        self.assertEqual(response.url, '{}{}'.format('/ad/post/', latest_post.id))