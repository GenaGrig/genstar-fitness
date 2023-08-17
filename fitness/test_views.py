import unittest
from fitness.views import MainPageView, MembershipView, WorkoutsView
from fitness.views import PersonalTrainerView, ContactView


class FitnessTest(unittest.TestCase):
    """Tests for fitness/views.py."""
    def test_main_page_view(self):
        self.assertEqual(MainPageView.template_name, 'index.html')

    def test_membership_view(self):
        self.assertEqual(MembershipView.template_name, 'membership.html')

    def test_workouts_view(self):
        self.assertEqual(WorkoutsView.template_name, 'workouts.html')

    def test_personal_trainer_view(self):
        self.assertEqual(PersonalTrainerView.template_name,
                         'personal_trainer.html')

    def test_contact_view(self):
        self.assertEqual(ContactView.template_name, 'contact.html')


if __name__ == '__main__':
    unittest.main()
