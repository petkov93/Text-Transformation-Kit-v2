"""            🧵 Python Text Transformation Toolkit  🧵
"""
import json
import random

import requests


# from pprint import pprint

# with open('prog_jokes.json' ,mode='w', encoding='utf-8') as file:
#     json.dump(jokes, file,ensure_ascii=False)

def print_welcome_screen():
    starting_text = ["🧠 Welcome to the Text Transformation Toolkit!",
                     "Choose a transformation:",
                     "-----------------------------------------------",
                     "1. Reverse Text ⬅️⬅️⬅️",
                     "2. Convert to Uppercase ⬆️⬆️⬆️",
                     "3. Convert to Lowercase ⬇️⬇️⬇️",
                     "4. Title Case ⬆️➡️➡️",
                     "5. Count Vowels 🅰️eℹ️🅾️u",
                     "6. Remove All Spaces ' '➡️''",
                     "7. Replace Vowels with ⭐",
                     "8. Check if Palindrome 👍/👎",
                     "9. Word Frequency Counter ➡️ word: count",
                     "10. Get random programming joke 😀",
                     "0. Get random prog. joke BUT from API 😀",
                     "-----------------------------------------------",
                     '',
                     ]
    for txt in starting_text:
        print(txt)


def get_choice():
    choice = -1
    text = ''
    while not (0 <= choice <= 10):
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if not (0 <= choice <= 10):
                print("❌ Invalid choice! Please try again!")
        except ValueError:
            print('❌ Please enter valid number!')

    if choice not in [0, 10]:
        text = input("Enter the text: ")
    return choice, text


def text_transform(chosen_number, txt_str):
    def text_reverse(text):
        return f'Reversed text:\n{text[::-1]}'

    def text_upper(text):
        return f'Text to Uppercase:\n{text.upper()}'

    def text_lower(text):
        return f'Text to Lowercase:\n{text.lower()}'

    def text_title(text):
        return f'Title case text:\n{text.title()}'

    def count_vowels(text):
        vowels_count = 0
        for letter in text:
            if letter in 'aeiou':
                vowels_count += 1
        return f'Vowels count: {vowels_count}'

    def remove_spaces(text):
        return f'Spaces removed:\n{text.replace(' ', '')}'

    def replace_vowels(text):
        text_list = ['*' if letter in 'aeiou' else letter for letter in text]
        return 'Vowels replaced with "*":\n' + ''.join(text_list)

    def is_palindrome(text):
        result = ''
        converted_text = text.lower().replace(' ', '')
        reversed_text = converted_text[::-1]
        if converted_text != reversed_text:
            result = 'NOT '
        return f'"{text}" is {result}a palindrome.'

    def word_frequency_counter(text):
        text_lst = text.lower().split(' ')
        dict1 = {}
        output_str = 'Word Frequency Counter:\n'
        for word in text_lst:
            if '.' in word:
                word.replace('.', '')
            word_count = text_lst.count(word)
            dict1.update({word: word_count})
        for key in dict1:
            output_str += f'{key} => {dict1[key]}\n'
        return output_str

    def print_random_joke(text):
        """Because I got bored..."""
        with open('jokes.json', mode='r', encoding='utf-8') as file:
            loaded_jokes = json.load(file)
        random_joke = random.choice(list(loaded_jokes.values()))
        return f'\n😀 {random_joke} 😀'

    def print_api_joke(text):
        """Because I got bored...again..."""
        jokes_url = 'https://v2.jokeapi.dev/joke/'
        endpoint = 'Programming'
        params = {
            'type': '',  # 'single' or 'twopart'
            'contains': '',  # search for something specific
            'blacklistFlags': '',  # Exclude inappropriate content
            "lang": "en",
        }
        with requests.get(jokes_url + endpoint, params=params) as response:
            if response.status_code == 200:
                data = response.json()
            else:
                return 'Oops!!! An error occurred while getting the response from API. Check params!/URL'

        if data['type'] == 'twopart':
            joke_text = (f'\n– {data['setup']} 🤔'
                         f'\n– {data['delivery']} 💁‍♂️')
        else:
            joke_text = f'\n 😀 {data['joke']} 😀'
        return joke_text

    # to avoid the annoying if-elif :D
    # binds the choice to the corresponding func
    functions = {
        1: text_reverse,
        2: text_upper,
        3: text_lower,
        4: text_title,
        5: count_vowels,
        6: remove_spaces,
        7: replace_vowels,
        8: is_palindrome,
        9: word_frequency_counter,
        0: print_api_joke,
        10: print_random_joke,
    }
    # gets the corresponding func from the functions
    selected_function = functions.get(chosen_number)
    # transforming the text
    txt_str = selected_function(txt_str)

    return txt_str


def main_func():
    # Step 1: Display a menu to the user
    print_welcome_screen()
    # Step 2: Get the user's choice
    # Step 3: Get the input string
    chosen_number, text = get_choice()
    # Step 4: Apply the selected transformation
    result = text_transform(chosen_number, text)
    print(f'{result}\n')


if __name__ == '__main__':
    main_func()
