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

     return {
        "breed": breed,
        "image": image_url
    }


def get_fox_info():
    """Gets random fox image"""
    url = "https://randomfox.ca/floof/"
    response = requests.get(url).json()

    return {
        "image": response["image"]
    }


