# -*- coding: utf-8 -*-

# Copyright 2015 Donne Martin. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.


# THIS CODE IS FOR PYTHON 3
from __future__ import unicode_literals
from __future__ import print_function
import sys
import unittest

from importlib import reload #This line makes compilation not work on python 2
# This is the actual syntax error for python2
foo = exec

class KeysTest(unittest.TestCase):

    def python3_code(obj):
        print("some text,", end="")
        print(' print more text on the same line')

    def copy_paste_error(a, b):
        if (a and b):
            x = x + z
        if (a and b):
            y = x + z # A COPY_PASTE_ERROR here

    def deadcode(o1):
        try:
            if(o1 is None):
                return 1
            if (None is o1):
			    # DEADCODE defect
                return 2
		        # otherwise
                return 3
        except NameError as err:
            print(err)


    def forward_null_example(obj):
        if (obj is not None):
            deadcode(1)
        # obj will be NULL on else branch of if
        return obj.foo # Defect here.

    def identical_branches(a, b, op):
        if (op == '+'): # Defect here.
            result = a + b
        else:
            result = a + b
        return result

    def constant_expression_result(val):
        if ~(val & 1): # A CONSTANT_EXPRESSION_RESULT here ('~' probably should be 'not')
            return None

    def identifier_typo_to_fix(obj):
        obj.mouseMoveAction.eventHandler = None
        obj.mouseClickAction.eventHandler = None
        obj.keyboardAction.eventHander = None    # Defect here.


    def foo(arg1, arg2, password):
        password = "password"
        return arg1 + arg2, password


    arg2 = "password"
    first_return, arg2 = foo(1, 2, arg2)

