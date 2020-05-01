from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model

from my_bs_app.models import Post

from .utils import create_image

User = get_user_model()


class TestPostView(TestCase):

    def setUp(self):
        self.user = User.objects.filter(username='test_user').first()
        if not self.user:
            self.user = User.objects.create_user(
                username='test_user',
                email='ney@test.com',
                password='123'
            )

    def test_create_no_request_data(self):
        before_create_posts_count = Post.objects.count()
        response = self.client.post(
            reverse('create_post')
        )
        after_create_posts_count = Post.objects.count()

        self.assertEqual(response.status_code, 200)
        # The count of posts should be the same before and after
        # the post because when there is not data an empty form is
        # renders with errors.
        self.assertEqual(
            before_create_posts_count,
            after_create_posts_count
        )
        self.assertIn(
            'This field is required',
            str(response.content)
        )

    def test_create_ok(self):
        img = create_image()
        img_file = SimpleUploadedFile('front.png', img.getvalue())

        client = Client()
        client.login(username=self.user.username, password='123')
        response = client.post(
            reverse('create_post'),
            data={'title': 'Post 1', 'content': 'Post 1 content', 'image': img_file},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Post 1'))
