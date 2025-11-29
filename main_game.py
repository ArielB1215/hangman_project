import random
from game_functions import(
    game_setup,
    display_and_feedback,
    input_and_validations,
    game_logic,
    game_state
)


word_list = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic",
    "melon"
]


# def choose_a_random_word(word_list: list):
    # random_index = random.randint(a=0, b=len(word_list) - 1)
    # return list_of_words[random_index]

# def print_hidden_word(word: str):
    # if word.isalpha() == False:
    #         return False
    # elif len(word) != 1:
    #     return False
    # else:
    #     return word

all_letters = "abcdefghijklmnopqrstuvwxyz"
max_number_of_guesses = 6

def main():
    print("Welcome to the hangman game!")
    secret_word = game_setup.choose_random_word(word_list)
    secret_letters_to_be_guessed = game_setup.initialize_letters_to_be_guessed(secret_word)
    list_of_alphabet_letters = game_setup.initialize_alphabet_display(all_letters)

    incorrect_guesses_count = 0
    user_guessed_letters = set()
    display_and_feedback.display_game_status(
        letters_alphabet=list_of_alphabet_letters,
        guessed_letters=user_guessed_letters,
        hidden_word=secret_word,
        attempts_remain=max_number_of_guesses - incorrect_guesses_count
    )

    while not game_state.is_game_over(
            hidden_letters=secret_letters_to_be_guessed,
            attempts_remaining= max_number_of_guesses - incorrect_guesses_count
    ):

        letter_from_input = input_and_validations.get_valid_guess(guessed_letters=user_guessed_letters)
        game_logic.update_guessed_letters(letter_from_input, user_guessed_letters)

        if game_logic.check_letter_in_word(letter_from_input, secret_word):
            # Correct guess
            # Update and remove correct letter from letters_to_be_guessed
            game_logic.update_letters_to_be_guessed(secret_letters_to_be_guessed, letter_from_input)
            if game_state.check_win_condition(hidden_letters=secret_letters_to_be_guessed):
                display_and_feedback.show_win_message(secret_word)
        else:
            # Incorrect guess
            # add +1 to incorrect guesses
            incorrect_guesses_count += 1
            display_and_feedback.show_hangman(incorrect_guesses=incorrect_guesses_count)
            if game_state.check_lose_condition(attempts_remaining=max_number_of_guesses - incorrect_guesses_count):
                display_and_feedback.show_lose_message(secret_word)

        # if game_state.check_win_condition(hidden_letters=user_guessed_letters):
            # display_and_feedback.show_win_message(secret_word)
        # elif game_state.check_lose_condition(attempts_remaining=max_number_of_guesses - incorrect_guesses_count):
            # display_and_feedback.show_lose_message(secret_word)

        display_and_feedback.display_game_status(
            letters_alphabet=list_of_alphabet_letters,
            guessed_letters=user_guessed_letters,
            hidden_word=secret_word,
            attempts_remain=max_number_of_guesses - incorrect_guesses_count
        )


if __name__ == '__main__':
    main()









