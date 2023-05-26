import unittest

from pyvalueobjects.errors.ValueObjectError import ValueObjectError
from pyvalueobjects.security.cve_id import CveId


class TestCveIdValueObject(unittest.TestCase):
    def test_value_return_input_value(self):
        vo = CveId('CVE-2023-33000')
        self.assertEqual('CVE-2023-33000', vo.value())

    def test_bad_format_cve_raise_error(self):
        self.assertRaises(ValueObjectError, CveId, 'no-format')

    def test_none_raise_error(self):
        self.assertRaises(ValueObjectError, CveId, None)