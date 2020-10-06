import unittest
import xml.etree.ElementTree as ET

from tind_commons.xmlutils import deep_equal

class DeepEqualTests(unittest.TestCase):
    def test_obviously_equal_documents(self):
        doc = "<a>1<b>2</b>d</a>"
        a_element = ET.fromstring(doc)
        b_element = ET.fromstring(doc)

        self.assertTrue(deep_equal(a_element, b_element))

    def test_tail_different_documents(self):
        a_doc = "<a>1<b>2</b></a>"
        b_doc = "<a>1<b>2</b> </a>"

        a_element = ET.fromstring(a_doc)
        b_element = ET.fromstring(b_doc)

        self.assertFalse(deep_equal(a_element, b_element))

    def test_attribute_order_is_insignificant(self):
        a_doc = """<a b="c" d="e"></a>"""
        b_doc = """<a d="e" b="c"></a>"""

        a_element = ET.fromstring(a_doc)
        b_element = ET.fromstring(b_doc)

        self.assertTrue(deep_equal(a_element, b_element))

    def test_namespace_aware(self):
        a_doc = """<a xmlns="foo"></a>"""
        b_doc = """<a xmlns="bar"></a>"""

        a_element = ET.fromstring(a_doc)
        b_element = ET.fromstring(b_doc)

        self.assertFalse(deep_equal(a_element, b_element))

    def test_namespace_prefix_aware(self):
        a_doc = """<x:a xmlns:x="foo"></x:a>"""
        b_doc = """<a xmlns="foo"></a>"""

        a_element = ET.fromstring(a_doc)
        b_element = ET.fromstring(b_doc)

        self.assertTrue(deep_equal(a_element, b_element))
