# -*- coding: utf-8 -*-

import os 
import pytest
import numpy as np
from nautilus_nlp.utils.file_loader import documents_loader, list_files, detect_encoding

testdoc_latin1 = "J'aime les frites bien grasse étalon châpeau!"
testdoc_utf8 = "Un deuxième exemple de texte en utf-8 cette fois!"


encoded_s = testdoc_latin1.encode('latin-1')
with open('testdoc_latin1.txt', 'wb') as f:
    f.write(encoded_s)


encoded_s = testdoc_utf8.encode('utf-8')
with open('testdoc_utf8.txt', 'wb') as f:
    f.write(encoded_s)


def test_openfile_with_encoding():
    input_str = "testdoc_latin1.txt"
    expected_str = testdoc_latin1
    result = documents_loader(input_str, encoding='latin-1')
    np.testing.assert_string_equal(result, expected_str)


def test_openfile_utf8():
    input_str = "testdoc_utf8.txt"
    expected_str = testdoc_utf8
    result = documents_loader(input_str)
    np.testing.assert_string_equal(result, expected_str)


def test_encoding_detection():
    input_str = "testdoc_latin1.txt"
    expected_str = testdoc_latin1
    result = documents_loader(input_str)
    np.testing.assert_string_equal(result, expected_str)    
  

def test_load_several_docs_wildcard():
    expected = {'testdoc_latin1.txt': "J'aime les frites bien grasse étalon châpeau!",
                'testdoc_utf8.txt': 'Un deuxième exemple de texte en utf-8 cette fois!'}
    result = documents_loader('*.txt', output_as='dict')
    np.testing.assert_equal(result, expected)   


def test_load_several_docs_list():
    expected = {'testdoc_latin1.txt': "J'aime les frites bien grasse étalon châpeau!",
                'testdoc_utf8.txt': 'Un deuxième exemple de texte en utf-8 cette fois!'}
    result = documents_loader(['testdoc_latin1.txt','testdoc_utf8.txt'], output_as='dict')
    np.testing.assert_equal(result, expected)


def test_load_several_docs_output_list():
    expected = ["J'aime les frites bien grasse étalon châpeau!",
                'Un deuxième exemple de texte en utf-8 cette fois!']
    result = documents_loader(['testdoc_latin1.txt','testdoc_utf8.txt'], output_as='list')
    return len(expected) == len(result) and sorted(expected) == sorted(result)


#@pytest.mark.parametrize("input_filepath", ['*.txt','','testfolder_fileloader'])
#def test_list_files(input_filepath):
#    expected = ['testdoc_latin1.txt','testdoc_utf8.txt']
#    result = list_files(input_filepath)
#   return len(expected) == len(result) and sorted(expected) == sorted(result)


def test_detect_encoding():
    expected = {'encoding': 'ISO-8859-1', 'confidence': 0.73, 'language': ''}
    result = detect_encoding('testdoc_latin1.txt')
    np.testing.assert_equal(result, expected)

os.remove('testdoc_latin1.txt')
os.remove('testdoc_utf8.txt')