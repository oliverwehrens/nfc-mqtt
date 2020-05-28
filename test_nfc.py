from unittest import TestCase

from nfc2mqtt_service import find_tag_type, get_id


class TestNfc(TestCase):

    def test_find_tag_types(self):
        tag_type = find_tag_type("Type2Tag 'NXP NTAG215' ID=XXXXXXX")
        self.assertEqual("Type2Tag", tag_type)

    def test_find_id(self):
        tag_type = get_id("Type2Tag 'NXP NTAG215' ID=04CEAAB2064F80")
        self.assertEqual("04CEAAB2064F80", tag_type)