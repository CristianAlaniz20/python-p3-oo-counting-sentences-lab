#!/usr/bin/env python3

import re

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
      self._value = new_value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    result = self.value.endswith(".")
    return result

  def is_question(self):
    result = self.value.endswith("?")
    return result

  def is_exclamation(self):
    result = self.value.endswith("!")
    return result

  def count_sentences(self):
        sentences = [sentence for sentence in re.split(r"[.!?]+", self.value) if sentence]
        return len(sentences)