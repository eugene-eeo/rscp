import string
import random

from unittest import TestCase
from rscp.burrows_wheeler_transform import transform, reverse


def generate_string(min=50, max=100):
    s = []
    for _ in range(random.randint(min, max)):
        s.append(random.choice(string.ascii_letters))
    return "".join(s)


class BurrowsWheelerTest(TestCase):
    def test_transform(self):
        assert transform("abraca") == ("caraab", 1)

    def test_reverse(self):
        assert reverse("caraab", 1) == "abraca"

    def test_transform_reverse(self):
        for _ in range(10):
            s = generate_string()
            assert reverse(*transform(s)) == s
