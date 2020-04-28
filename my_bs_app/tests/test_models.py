from django.test import TestCase
from django.contrib.auth import get_user_model

from my_bs_app.models import Post


User = get_user_model()


class TestPost(TestCase):

    def setUp(self):
        self.user = User.objects.filter(username='test_user').first()
        if not self.user:
            self.user = User.objects.create_user(
                username='test_user',
                email='ney@test.com',
                password='123'
            )

    def test_create(self):
        p = Post.objects.create(title='This is a title', author=self.user)

        self.assertEqual(p.title, 'This is a title')

    def test_update(self):
        p, created = Post.objects.get_or_create(title='This is a title', author=self.user)
        p.title = 'This is another title'
        p.save()

        self.assertEqual(p.title, 'This is another title')

    def test_delete(self):
        p, created = Post.objects.get_or_create(title='This is a second title', author=self.user)
        p_pk = p.pk

        Post.objects.filter(pk=p_pk).delete()

        self.assertFalse(Post.objects.filter(pk=p_pk).exists())