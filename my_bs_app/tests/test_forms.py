from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from my_bs_app.forms import PostForm, NewUserForm

from .utils import create_image


class PostFormTest(TestCase):

    def test_post_form_unbound(self):
        form = PostForm()

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.fields['title'].label,
            'Title'
        )

    def test_new_user_form_unbound(self):
        form = NewUserForm()

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.fields['username'].label,
            'Username'
        )

    def test_post_form_bound(self):
        img = create_image()
        img_file = SimpleUploadedFile('front.png', img.getvalue())
        form = PostForm(
            data={'title': 'Post 1', 'content': 'Post 1 content',},
            files={'image': img_file}
        )

        self.assertTrue(form.is_valid())

    def test_new_user_form_bound(self):
        form = NewUserForm(
            data={
                "username": "test_u",
                "email": "test@gmail.com",
                "password1": "Phhhaa123**",
                "password2": "Phhhaa123**"
            }
        )

        self.assertTrue(form.is_valid())
