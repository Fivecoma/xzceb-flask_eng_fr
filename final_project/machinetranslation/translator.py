"""
This module allows you to translate text from french to english and from english to french
"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_lang_trans_instance():
    """
    Create a Language Translator instance and return it
    """
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2022-01-11',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator

def englishToFrench(english_text):
    """
    Translate english text to french text with a Language Translator instance
    """
    language_translator = create_lang_trans_instance()
    translation = language_translator.translate(
    english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    Translate french text to english text with a Language Translator instance
    """
    language_translator = create_lang_trans_instance()
    translation = language_translator.translate(
    french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
