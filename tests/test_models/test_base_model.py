#!/usr/bin/python3
import unittest
import directory
from datetime import datetime, timedelta
import models.base_model as md
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        This module is a test case of the BaseModel
    """
    def test_created_at(self):
        """
            This is to check the created_at attribute
        """
        obj = BaseModel()
        self.assertTrue(isinstance(obj.created_at, datetime))
        now = datetime.now()
        self.assertTrue(now - timedelta(seconds=1) < obj.created_at < now
                        + timedelta(seconds=1))

    def test_updated_at(self):
        """
            This is to check the updated_at attribute
        """
        obj = BaseModel()
        obj.save()
        now = datetime.now()
        self.assertTrue(now - timedelta(seconds=1) < obj.updated_at < now
                        + timedelta(seconds=1))

    def test_documentation(self):
        obj = BaseModel()
        print("Module Documentation")
        self.assertIsNotNone(md.__doc__)
        print("Class Documentation")
        self.assertIsNotNone(obj.__doc__)
        print("__init__ Documentation")
        self.assertIsNotNone(obj.__init__.__doc__)
        print("Save Documentation")
        self.assertIsNotNone(obj.save.__doc__)
        print("to_dict Documentation")
        self.assertIsNotNone(obj.to_dict.__doc__)


if __name__ == "__main__":
    unittest.main()
