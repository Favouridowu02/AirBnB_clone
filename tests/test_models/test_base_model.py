#!/usr/bin/python3
import sys
import os
import unittest
from datetime import datetime, timedelta

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, parent_dir)
import models
from models.base_model import BaseModel
import models.base_model as md

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
        self.assertTrue(now - timedelta(seconds=1) < obj.created_at < now + timedelta(seconds=1))

    def test_updated_at(self):
        """
            This is to check the updated_at attribute
        """
        obj = BaseModel()
        obj.save()
        now = datetime.now()
        self.assertTrue(now - timedelta(seconds=1) < obj.updated_at < now + timedelta(seconds=1))


    def test_documentation(self):
        obj = BaseModel()
        print("Module Documentation")
        self.assertTrue(md.__doc__ != None)
        print("Class Documentation")
        self.assertTrue(obj.__doc__ != None)
        print("__init__ Documentation")
        self.assertTrue(obj.__init__.__doc__ != None)
        print("Save Documentation")
        self.assertTrue(obj.save.__doc__ != None)
        print("to_dict Documentation")
        self.assertTrue(obj.to_dict.__doc__ != None)

if __name__ == "__main__":
    unittest.main()
