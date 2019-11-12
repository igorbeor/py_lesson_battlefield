from unittest import TestCase
from classes.units.solider import Solider
from classes.rand import Rand


class SoliderTest(TestCase):
    def setUp(self):
        Rand.seed(123)
        self.solider = Solider()

    def test_experience(self):
        self.solider.experience = 60
        self.assertEqual(self.solider.experience, 50)
        self.solider.experience = -10
        self.assertEqual(self.solider.experience, 0)

    def test_attack_success(self):
        self.solider.experience = 50
        self.solider.health = 100
        attack_success = self.solider.attack_success
        self.assertGreaterEqual(attack_success, 0)
        self.assertLessEqual(attack_success, 1)
        self.solider.experience = 0
        self.solider.health = 0
        attack_success = self.solider.attack_success
        self.assertGreaterEqual(attack_success, 0)
        self.assertLessEqual(attack_success, 1)

    def test_damage(self):
        self.solider.experience = 0
        self.assertEqual(self.solider.damage, 0.05)
        self.solider.experience = 50
        self.assertEqual(self.solider.damage, 0.55)

    def test_is_active(self):
        self.solider.health = 10
        self.assertEqual(self.solider.is_active, True)
        self.solider.health = 0
        self.assertEqual(self.solider.is_active, False)

    def test_get_damage(self):
        self.solider.health = 100
        self.solider.get_damage(120)
        self.assertEqual(self.solider.health, 0)

    def test_experience_gain(self):
        self.solider.experience = 50
        self.solider.experience_gain()
        self.assertEqual(self.solider.experience, 50)
