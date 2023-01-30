from django.shortcuts import render
from .task import *

def test_func():
    generate_file.delay("test",10)
