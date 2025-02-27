from datetime import datetime
from .pdf_handler import get_content
import os
from project.settings import BASE_DIR
from .bert_handler import *
import random
from nltk.corpus import wordnet

# y = random.randrange(size)
question_templates = [

    'Write a short description on _',
    'What is _ ?'
]
import random

def get_synonyms(word):
  
  synonyms = []

  for syn in wordnet.synsets(word):
    for i in syn.lemmas():
      synonyms.append(i.name())
  print('Synonyms', synonyms)
  return synonyms

def get_antonyms(word):
  antonyms = []
  for syn in wordnet.synsets(word):
    for i in syn.lemmas():
      if i.antonyms():
        antonyms.append(i.antonyms()[0].name())
  print('antonyms', antonyms)
  return antonyms


def generate_all_questions(doc_contents):
  question_bank1_list = []
  question_bank2_list = []
  question_bank3_list = []
  ########### Document Processing ###################
    # question_bank1 - id, user_id, doc_id, question, answer, mark
    # question_bank2 - id, user_id, doc_id, question, answer, mark
    # question_bank3 - id, user_id, doc_id, question, op1, op2, op3, op4, answer, mark
  i = 1
  for doc_content in doc_contents:
    keywords=get_keywords(doc_content)
    for keyword in keywords:
      y = random.randrange(len(question_templates))
      question2 = question_templates[y]
      question2 = question2.replace('_',keyword)
      answer2 = doc_content
      question_bank2_list.append({'question2':question2, 'answer2':answer2})
    
      
    summary_list=get_summary(doc_content)
    for summary_text in summary_list:
      question1 = ''
      answer1 = ''
      try:
        temp_key = get_keywords(summary_text)                
        question1 = summary_text
        for t in temp_key:
          #question1 = question1.replace(t,'_')
          #answer1 = ','.join(temp_key)
          question_bank1_list.append({'question1':question1.lower().replace(t.lower(),'_'), 'answer1':t})

          question3 = question1.lower().replace(t.lower(),'_')#'Question '+ str(i)
          op_list = []
          op_list.append(t)
          w_list = []
          s_list = get_synonyms(t)
          w_list.extend(s_list)
          for s in s_list:
            a_list = get_antonyms(s)
            w_list.extend(a_list)
          w2_list = []
          for w in set(w_list):
            w2_list.append(w)
          print('#############',w2_list)
          op_list.extend(w2_list)
          random.shuffle(op_list)
          if len(op_list) >=4:
            op1 = op_list[0]
            op2 = op_list[1]
            op3 = op_list[2]
            op4 = op_list[3]
            answer=t
            question_bank3_list.append({'question3':question3, 'op1':op1, 'op2':op2, 'op3':op3, 'op4':op4,'answer':answer})

      except Exception as e:
        print('Err>>', e)
        continue

    i +=1
  ################################
  return question_bank1_list, question_bank2_list, question_bank3_list