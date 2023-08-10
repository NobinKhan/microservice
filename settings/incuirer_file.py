# Development Settings

import inquirer

def base_choices_select(choices, message):
    questions = [
        inquirer.List(
            'choice',
            message=message,
            choices=choices,
        ),
    ]

    answers = inquirer.prompt(questions, raise_keyboard_interrupt=True)

    return answers['choice']



def main():
    databases = ("MySQL", "Postgresql", "NoSQL")
    try:
        selected = base_choices_select(choices=databases, message="Select database: ")
        print("You have selected {} database.".format(selected))
    except KeyboardInterrupt:
        print("Se you not for mind!")

    




if __name__ == "__main__":
    main()

