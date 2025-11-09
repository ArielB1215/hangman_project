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

def print_hidden_word(word: str):
    if word.isalpha() == False:
            return False
    elif len(word) != 1:
        return False
    else:
        return word


if __name__ == '__main__':
    print(choose_a_random_word(list_of_words))
    new_word = input("Enter a new letter: ")
    print(print_hidden_word(new_word))









