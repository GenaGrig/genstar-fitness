import unittest

from fitness.forms import SignUpForm


class FitnessTest(unittest.TestCase):
    """Tests for fitness/forms.py."""
    def test_sign_up_form(self):
        form = SignUpForm()
        self.assertEqual(form.Meta.model.__name__, 'User')
        self.assertEqual(form.Meta.fields, ('username', 'email', 'password1',
                                            'password2'))
        self.assertEqual(form.Meta.fields[0], 'username')
        self.assertEqual(form.Meta.fields[1], 'email')
        self.assertEqual(form.Meta.fields[2], 'password1')
        self.assertEqual(form.Meta.fields[3], 'password2')
        self.assertEqual(form.fields['username'].label, '')
        self.assertEqual(form.fields['username'].help_text,
                         '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>')
        self.assertEqual(form.fields['email'].label, '')
        self.assertEqual(form.fields['email'].help_text,
                         '<span class="form-text text-muted"><small>Required.</small></span>')
        self.assertEqual(form.fields['password1'].label, '')
        self.assertEqual(form.fields['password1'].help_text,
                         '<ul class="form-text text-muted small"><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>')
        self.assertEqual(form.fields['password2'].label, '')
        self.assertEqual(form.fields['password2'].help_text,
                         '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>')
        self.assertEqual(form.fields['username'].widget.attrs['class'],
                         'form-control')
        self.assertEqual(form.fields['username'].widget.attrs['placeholder'],
                         'Username')
        self.assertEqual(form.fields['email'].widget.attrs['class'],
                         'form-control')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'],
                         'Email Address')
        self.assertEqual(form.fields['password1'].widget.attrs['class'],
                         'form-control')
        self.assertEqual(form.fields['password1'].widget.attrs['placeholder'],
                         'Password')
        self.assertEqual(form.fields['password2'].widget.attrs['class'],
                         'form-control')
        self.assertEqual(form.fields['password2'].widget.attrs['placeholder'],
                         'Confirm Password')
        self.assertEqual(form.fields['email'].required, True)
        self.assertEqual(form.fields['username'].required, True)
        self.assertEqual(form.fields['password1'].required, True)
        self.assertEqual(form.fields['password2'].required, True)


if __name__ == '__main__':
    unittest.main()
