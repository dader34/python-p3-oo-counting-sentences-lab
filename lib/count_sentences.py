#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
    if(type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self,value):
    if(type(value) == str):
      self._value = value
    else:
      print("The value must be a string.")


  def is_sentence(self):
    if(self._value[len(self._value)-1] == "."):
      return True
    else:
      return False
    
  def is_question(self):
    if(self._value[len(self._value)-1] == "?"):
      return True
    else:
      return False

  def is_exclamation(self):
      if(self._value[len(self._value)-1] == "!"):
        return True
      else:
        return False
    
  def count_sentences(self):
    sentence_count = 0
    sentence_ending_punctuation = ".!?"

    in_sentence = False
    for char in self._value:
        if char in sentence_ending_punctuation:
            if not in_sentence:
                sentence_count = sentence_count + 1
                in_sentence = True
        else:
            in_sentence = False

    return sentence_count
  
    


f = MyString("Hello!")
