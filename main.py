import requests
import tkinter as tk
from tkinter import messagebox

# API FUNCTIONS

def get_dog_info():
    """Gets random dog breed image + breed info"""
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url).json()

    image_url = response["message"]

    # Try to extract breed from URL
    breed = image_url.split("/")[4].replace("-", " ")

