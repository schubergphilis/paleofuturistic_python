from unittest import TestCase

from {{ cookiecutter.project_slug }} import hello


class TestSmoke(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_integration(self):
        self.assertEqual("Hello from {{ cookiecutter.project_slug }}!", hello())
