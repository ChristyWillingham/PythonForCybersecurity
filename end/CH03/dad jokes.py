#!/usr/bin/env python3
# Dad Jokes
#By Christy Willingham
# date: 8/10/25

import requests

def get_random_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        joke_data = response.json()
        return joke_data["joke"]
    except requests.exceptions.RequestException as e:
        print(f'Error fetching joke: {e}')
        return "Failed to retrieve a dad joke. "
if __name__== "__main__":
    joke = get_random_dad_joke()
    print(joke)