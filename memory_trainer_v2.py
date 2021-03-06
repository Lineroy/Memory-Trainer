from random import randint  # Random number, how we will compare.
from time import sleep  # Time for think, wait and etc.
from colorama import init, Fore, Style  # View of program!
from os import system  # For clearing console.
from ctypes import windll  # Calculation of the system language, the first process.
import locale  # Calculation of the system language, the second process.

init(autoreset=True)

# Language of the program(Begin);
windll = windll.kernel32
windll.GetUserDefaultUILanguage()

if locale.windows_locale[windll.GetUserDefaultUILanguage()] == "ru_UA" or "ru_RU":
    language = 2
else:
    language = 1


# Language of the program(End);


def cls():
    """
    Clear display from symbols.
    :return:
    """
    system("CLS || clear")


def cls_up_or_down(mtp=10):
    """
    Make 'umn' step to up or down.
    :param mtp:
    :return:
    """
    print("\n" * mtp)


how_numbers = "1"

# Counter, when we said correct number, when - no.
counter_True, counter_False = 0, 0

cls()
# Information for use(Begin);
print(
    "You must remember the number to be displayed." if language == 1
    else "Вы должны запомнить число которое будет выводиться на экран.")
sleep(3)

print(
    "If You want to change the settings, press the 'Space', there will be a menu with settings." if language == 1
    else "Если Вы захотите изменить настройки, нажмите 'Пробел', там будет меню с настройками.")
sleep(3)
# Information for use(End);

# Question to significant and time(Begin);
while True:
    try:
        how_len_number = int(input(
            "\nHow much significant will your number be?: " if language == 1
            else "Сколько значное будет ваше число?: "))

        break
    except ValueError:
        pass

while True:
    try:
        how_time_number = int(input("How long will it take for memorizing numbers?: " if language == 1
                                    else "Сколько времени потребуется для запоминания чисел?: "))

        break
    except ValueError:
        pass
# Question to significant and time(End);

# Adding numbers to the number we set earlier;
while len(how_numbers) != how_len_number:
    how_numbers += "0"

# Main process of the program(Begin);
while True:

    # Generation random number;
    random_number = randint(int(how_numbers), 9 * int(how_numbers))

    # Remember;
    print("\nRemember: " + Style.BRIGHT + Fore.YELLOW + str(random_number) if language == 1
          else "\nЗапомните: " + Style.BRIGHT + Fore.YELLOW + str(random_number))

    # Time to remember number;
    sleep(how_time_number)

    # Clear display after wait;
    cls()

    # Question to enter the number;
    how_the_number = input("Enter the number: " if language == 1 else "Введите число: ")

    # Question to settings and etc.(Begin);
    if how_the_number == "":
        cls()
        print(
            "\nIf you really want to end the process, here are the commands: \n- If you want to exit, press space; "
            "\n- If you want to continue, enter number - '6'; \n- If you want to change the settings - enter 'Set'; "
            "\n- If you want to change language of program - 'Lang'."

            if language == 1
            else "\nЕсли Вы действительно хотите закончить процесс, вот команды:\n- Если Вы хотите выйти, нажмите пробелл;"
                 "\n- Если хотите продолжить введите число - '6'; \n- Если вы захотите изменить настройки - введите 'Пар';"
                 "\n- Если Вы хотите изменить язык программы - 'Язык'.")

        ask_exit = input(">>> ")

        # Exit from program;
        if ask_exit == "":
            cls()
            print( Fore.YELLOW +
                    '██╗░░██╗░█████╗░██╗░░░██╗███████╗░░░█████╗░░░░██████╗░░█████╗░░█████╗░██████╗░\n'
                    '██║░░██║██╔══██╗██║░░░██║██╔════╝░░██╔══██╗░░██╔════╝░██╔══██╗██╔══██╗██╔══██╗\n'
                    '███████║███████║╚██╗░██╔╝█████╗░░░░███████║░░██║░░██╗░██║░░██║██║░░██║██║░░██║\n'
                    '██╔══██║██╔══██║░╚████╔╝░██╔══╝░░░░██╔══██║░░██║░░╚██╗██║░░██║██║░░██║██║░░██║\n'
                    '██║░░██║██║░░██║░░╚██╔╝░░███████╗░░██║░░██║░░╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝\n'
                    '╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░░╚═╝░░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚═════╝░\n'
                   
                                            '\t\t\t████████╗██╗███╗░░░███╗███████╗\n'
                                            '\t\t\t╚══██╔══╝██║████╗░████║██╔════╝\n'
                                            '\t\t\t░░░██║░░░██║██╔████╔██║█████╗░░\n'
                                            '\t\t\t░░░██║░░░██║██║╚██╔╝██║██╔══╝░░\n'
                                            '\t\t\t░░░██║░░░██║██║░╚═╝░██║███████╗\n'
                                            '\t\t\t░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝\n')

            sleep(2)
            cls()
            break

        # Continue of the program;
        elif ask_exit == "6":
            continue

        elif ask_exit.lower().startswith("lang") or ask_exit.lower().startswith("язык"):
            change_language = None
            while True:
                try:
                    cls()
                    print("Enter number of language how you will use: \n1) English(ENG); \n2) Russian(RU)."
                    if language == 1 else "Введите номер языка который Вы хотите использовать: \n1) Английский(ENG); \n2) Русский(RU).")

                    language = int(input(">>> "))

                    if language == 1 or 2:
                        print("Language has been changed!" if language == 1 else "Язык был изменён!")
                        sleep(1)
                        cls()
                        break

                except ValueError:
                    pass

        # Settings(Begin);
        elif ask_exit.lower().startswith("set" or "пар" or "пар"):
            while True:
                cls()
                # Information;
                print("\n"
                      f"1) Memorization time: {how_time_number} seconds;\n"
                      f"2) Number of values: {how_len_number} values." if language == 1 else
                      f"1) Время запоминания: {how_time_number} секунд;\n"
                      f"2) Количество значений: {how_len_number} значений."
                      )
                sleep(1)

                # What to change?;
                while True:
                    try:
                        how_setting = int(input("Enter number of parameter how You want to change: " if language == 1
                                                else "Введите номер параметра, который вы хотите изменить: "))

                        if how_numbers == 1 or 2:
                            break
                    except ValueError:
                        pass

                # Time to remember;
                if how_setting == 1:
                    while True:
                        try:
                            how_time_number = int(input("How long will it take for memorizing numbers?: "
                                                        if language == 1
                                                        else "Сколько времени потребуется для запоминания чисел?: "))

                            break
                        except ValueError:
                            continue

                # Significance of number;
                if how_setting == 2:
                    while True:
                        try:
                            how_len_number = int(input(
                                "\nHow much significant will Your number be?: " if language == 1
                                else "Сколько значное будет Ваше число?: "))

                            if how_len_number <= 0:
                                print("You entered a number equal to zero or less, please try again.")
                            else:
                                how_numbers = "1"
                                while len(how_numbers) != how_len_number:
                                    how_numbers += "0"

                                break
                        except ValueError:
                            continue

                # Exit from settings;
                continue_or_again = input(f"\nDo You want to exit the settings?(Y, N): " if language == 1
                                          else f"\nВы хотите выйти с настроек?(Д, Н): ").upper()

                if continue_or_again.upper().startswith("Y") or continue_or_again.upper().startswith("Д"):
                    break
                if continue_or_again.upper().startswith("N") or continue_or_again.upper().startswith("Н"):
                    pass

        # Wrong command;
        else:
            print("\nTry again write command!" if language == 1 else "Попробуйте ещё раз ввести команду!")
            continue

    # Question to settings and etc.(End);

    # Print of answer(Begin);
    try:
        # Right answer;
        if int(how_the_number) == random_number:
            cls()
            cls_up_or_down()
            print(Fore.GREEN +
                  '                     ██████╗░██╗░██████╗░██╗░░██╗████████╗██╗\n'
                  '                     ██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝██║\n'
                  '                     ██████╔╝██║██║░░██╗░███████║░░░██║░░░██║\n'
                  '                     ██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░╚═╝\n'
                  '                     ██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██╗\n'
                  '                     ╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝\n' if language == 1 else

                  Fore.GREEN + '                    ██████╗░███████╗██████╗░██╗░░██╗░█████╗░██╗\n'
                               '                    ██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██║\n'
                               '                    ██████╦╝█████╗░░██████╔╝███████║██║░░██║██║\n'
                               '                    ██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║╚═╝\n'
                               '                    ██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝██╗\n'
                               '                    ╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝\n')
            cls_up_or_down(7)

            counter_True += 1

            sleep(3)

        # Wrong answer;
        else:
            cls()
            cls_up_or_down()
            print(Fore.RED +
                  '         ███╗░░██╗░█████╗░████████╗░░████████╗██████╗░██╗░░░██╗███████╗██╗\n'
                  '         ████╗░██║██╔══██╗╚══██╔══╝░░╚══██╔══╝██╔══██╗██║░░░██║██╔════╝██║\n'
                  '         ██╔██╗██║██║░░██║░░░██║░░░░░░░░██║░░░██████╔╝██║░░░██║█████╗░░██║\n'
                  '         ██║╚████║██║░░██║░░░██║░░░░░░░░██║░░░██╔══██╗██║░░░██║██╔══╝░░╚═╝\n'
                  '         ██║░╚███║╚█████╔╝░░░██║░░░░░░░░██║░░░██║░░██║╚██████╔╝███████╗██╗\n'
                  '         ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝\n' if language == 1 else

                  Fore.RED + '          ██╗░░██╗███████╗░░██████╗░███████╗██████╗░██╗░░██╗░█████╗░██╗\n'
                             '          ██║░░██║██╔════╝░░██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██║\n'
                             '          ███████║█████╗░░░░██████╦╝█████╗░░██████╔╝███████║██║░░██║██║\n'
                             '          ██╔══██║██╔══╝░░░░██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║╚═╝\n'
                             '          ██║░░██║███████╗░░██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝██╗\n'
                             '          ╚═╝░░╚═╝╚══════╝░░╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝\n')

            cls_up_or_down(7)

            counter_False += 1

            sleep(3)
    except ValueError:
        continue

    # Answer errors or correct answer(Begin);
    decomposition_one = ", ".join(str(random_number)).split(", ")
    decomposition_two = ", ".join(how_the_number).split(", ")

    combination = []

    counter = 0

    for i in decomposition_one:
        try:
            if i == decomposition_two[counter]:
                combination.append(Style.BRIGHT + Fore.GREEN + decomposition_two[counter])
            else:
                combination.append(Style.BRIGHT + Fore.RED + decomposition_two[counter])

            counter += 1

        except IndexError:
            break

    print(Style.BRIGHT + Fore.GREEN + f"{'Question' if language == 1 else 'Вопрос'}: {str(random_number)}" + ' → '
          + f"{'Answer' if language == 1 else 'Ответ'}: {''.join(combination)}" + "\n")
    # Answer errors or correct answer(End);

    # Conclusion of all answers: True or False;
    print(
        Style.BRIGHT + f"{'Answers' if language == 1 else 'Ответ'}: " + (Fore.GREEN + Style.BRIGHT + str(counter_True)),
        "/",
        (Fore.RED + Style.BRIGHT + str(counter_False)))
# Main process of the program(End);
