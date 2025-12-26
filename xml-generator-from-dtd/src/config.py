"""
Contains the configuration needed for the forms
"""
import os


class Config:
    """
    Contains the SECRET_KEY needed for the forms
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qiwhhschvwevqe12093uqwh2'
