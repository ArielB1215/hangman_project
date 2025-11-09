import random

print("Welcome to the Hangman game!")

list_of_words = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic",
    "melon"
]


def choose_a_random_word(word_list: list):
    random_index = random.randint(a=0, b=len(word_list) - 1)
    return list_of_words[random_index]

def print_hidden_word(word):
    ...


if __name__ == '__main__':
    print(choose_a_random_word(list_of_words))









