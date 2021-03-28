from random import randint  # Random number, how we will compare.
from time import sleep  # Time for think, wait and etc.
from datetime import datetime
from colorama import init, Fore, Style  # View of program!
from ctypes import windll  # Calculation of the system language, the first process.
import os  # For clearing console.
import sys
import threading
import keyboard
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
    os.system("CLS || clear")


def cls_down(mtp=10):
    """
    Make 'umn' step to up or down.
    :param mtp:
    :return:
    """
    print("\n" * mtp)


def for_honesty(seconds):
    event = threading.Event()
    event.set()

    def back_timer():
        event.clear()

    threading.Timer(seconds, back_timer).start()

    while event.is_set():
        def pressed_keys(e):
            if e.name in [str(n) for n in range(0, 10)]:
                if not event.is_set():
                    event.clear()
                else:
                    keyboard.press("backspace")

        keyboard.hook(pressed_keys)
        keyboard.wait()


how_numbers = "1"

windows_version = sys.getwindowsversion().platform_version[0]

# Counter, when we said correct number, when - no.
counter_True, counter_False = 0, 0

changed_values = 0

memorization_combo = 1

congratulation = {1: '                     ██████╗░██╗░██████╗░██╗░░██╗████████╗██╗\n'
                     '                     ██╔══██╗██║██╔════╝░██║░░██║╚══██╔══╝██║\n'
                     '                     ██████╔╝██║██║░░██╗░███████║░░░██║░░░██║\n'
                     '                     ██╔══██╗██║██║░░╚██╗██╔══██║░░░██║░░░╚═╝\n'
                     '                     ██║░░██║██║╚██████╔╝██║░░██║░░░██║░░░██╗\n'
                     '                     ╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝\n',
                  2: '                        ░██████╗░░█████╗░░░░░░█████╗░███╗░░██╗██╗\n'
                     '                        ██╔════╝░██╔══██╗░░░░██╔══██╗████╗░██║██║\n'
                     '                        ██║░░██╗░██║░░██║░░░░██║░░██║██╔██╗██║██║\n'
                     '                        ██║░░╚██╗██║░░██║░░░░██║░░██║██║╚████║╚═╝\n'
                     '                        ╚██████╔╝╚█████╔╝░░░░╚█████╔╝██║░╚███║██╗\n'
                     '                        ░╚═════╝░░╚════╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝\n',
                  3: '███╗░░██╗███████╗██╗░░░██╗███████╗██████╗░░░░██████╗░██╗██╗░░░██╗███████╗░░██╗░░░██╗██████╗░██╗\n'
                     '████╗░██║██╔════╝██║░░░██║██╔════╝██╔══██╗░░██╔════╝░██║██║░░░██║██╔════╝░░██║░░░██║██╔══██╗██║\n'
                     '██╔██╗██║█████╗░░╚██╗░██╔╝█████╗░░██████╔╝░░██║░░██╗░██║╚██╗░██╔╝█████╗░░░░██║░░░██║██████╔╝██║\n'
                     '██║╚████║██╔══╝░░░╚████╔╝░██╔══╝░░██╔══██╗░░██║░░╚██╗██║░╚████╔╝░██╔══╝░░░░██║░░░██║██╔═══╝░╚═╝\n'
                     '██║░╚███║███████╗░░╚██╔╝░░███████╗██║░░██║░░╚██████╔╝██║░░╚██╔╝░░███████╗░░╚██████╔╝██║░░░░░██╗\n'
                     '╚═╝░░╚══╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═════╝░╚═╝░░░╚═╝░░░╚══════╝░░░╚═════╝░╚═╝░░░░░╚═╝\n'
                  }

cls()

how_len_number, how_time_number = None, None
memory_trainer_view_seconds, version_seconds = 0.25, 0.05
button_space = 3

while None in [how_len_number, how_time_number]:
    cls()
    window_counter = 0

    if windows_version in [8, 10]:
        sys.stdout.write("\n" * 2 + Fore.LIGHTBLACK_EX + Style.BRIGHT +
                         '                  ██╗░░██╗░█████╗░██╗░░░░░░█████╗░░░░░░░█████╗░███╗░░░███╗██╗░██████╗░░█████╗░██╗\n'
                         '                  ██║░░██║██╔══██╗██║░░░░░██╔══██╗░░░░░██╔══██╗████╗░████║██║██╔════╝░██╔══██╗██║\n'
                         '                  ███████║██║░░██║██║░░░░░███████║░░░░░███████║██╔████╔██║██║██║░░██╗░██║░░██║██║\n'
                         '                  ██╔══██║██║░░██║██║░░░░░██╔══██║██╗░░██╔══██║██║╚██╔╝██║██║██║░░╚██╗██║░░██║╚═╝\n'
                         '                  ██║░░██║╚█████╔╝███████╗██║░░██║╚█║░░██║░░██║██║░╚═╝░██║██║╚██████╔╝╚█████╔╝██╗\n'
                         '                  ╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝░╚╝░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚════╝░╚═╝\n\n\n')

        memory_trainer_view = [
            "   ███╗░░░███╗███████╗███╗░░░███╗░█████╗░██████╗░██╗░░░██╗░████████╗██████╗░░█████╗░██╗███╗░░██╗███████╗██████╗░",
            "   ████╗░████║██╔════╝████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝░╚══██╔══╝██╔══██╗██╔══██╗██║████╗░██║██╔════╝██╔══██╗",
            "   ██╔████╔██║█████╗░░██╔████╔██║██║░░██║██████╔╝░╚████╔╝░░░░░██║░░░██████╔╝███████║██║██╔██╗██║█████╗░░██████╔╝",
            "   ██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██║░░██║██╔══██╗░░╚██╔╝░░░░░░██║░░░██╔══██╗██╔══██║██║██║╚████║██╔══╝░░██╔══██╗",
            "   ██║░╚═╝░██║███████╗██║░╚═╝░██║╚█████╔╝██║░░██║░░░██║░░░░░░░██║░░░██║░░██║██║░░██║██║██║░╚███║███████╗██║░░██║",
            "   ╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝\n\n"]

        for part in memory_trainer_view:
            print(Fore.LIGHTRED_EX + part)
            sleep(memory_trainer_view_seconds)
    else:
        print(Fore.LIGHTBLACK_EX +
              '██╗░░██╗░█████╗░██╗░░░░░░█████╗░░░░░░░█████╗░███╗░░░███╗██╗░██████╗░░█████╗░██╗\n'
              '██║░░██║██╔══██╗██║░░░░░██╔══██╗░░░░░██╔══██╗████╗░████║██║██╔════╝░██╔══██╗██║\n'
              '███████║██║░░██║██║░░░░░███████║░░░░░███████║██╔████╔██║██║██║░░██╗░██║░░██║██║\n'
              '██╔══██║██║░░██║██║░░░░░██╔══██║██╗░░██╔══██║██║╚██╔╝██║██║██║░░╚██╗██║░░██║╚═╝\n'
              '██║░░██║╚█████╔╝███████╗██║░░██║╚█║░░██║░░██║██║░╚═╝░██║██║╚██████╔╝╚█████╔╝██╗\n'
              '╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝░╚╝░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░╚═════╝░░╚════╝░╚═╝\n')

        memory_trainer_view = [' ███╗░░░███╗███████╗███╗░░░███╗░█████╗░██████╗░██╗░░░██╗░░████████╗██████╗░░░░',
                               ' ████╗░████║██╔════╝████╗░████║██╔══██╗██╔══██╗╚██╗░██╔╝░░╚══██╔══╝██╔══██╗░░░',
                               ' ██╔████╔██║█████╗░░██╔████╔██║██║░░██║██████╔╝░╚████╔╝░░░░░░██║░░░██████╔╝░░░',
                               ' ██║╚██╔╝██║██╔══╝░░██║╚██╔╝██║██║░░██║██╔══██╗░░╚██╔╝░░░░░░░██║░░░██╔══██╗░░░',
                               ' ██║░╚═╝░██║███████╗██║░╚═╝░██║╚█████╔╝██║░░██║░░░██║░░░░░░░░██║░░░██║░░██║██╗',
                               ' ╚═╝░░░░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝\n']

        for part in memory_trainer_view:
            print(Fore.RED + part)
            sleep(memory_trainer_view_seconds)

    version = [
        ('       ██╗░░░█', '       ██║░░░█', '       ╚██╗░██', '       ░╚████╔', '       ░░╚██╔╝', '       ░░░╚═╝░'),
        ('█╗██████', '█║██╔═══', '╔╝█████╗', '╝░██╔══╝', '░░██████', '░░╚═════'),
        ('█╗█████', '═╝██╔══', '░░█████', '░░██╔══', '█╗██║░░', '═╝╚═╝░░'),
        ('█╗░░█████', '██╗██╔═══', '█╔╝╚█████', '██╗░╚═══█', '██║██████', '╚═╝╚═════'),
        ('█╗██╗░█', '═╝██║██', '╗░██║██', '█╗██║██', '╔╝██║╚█', '╝░╚═╝░╚'),
        ('████╗░██', '╔══██╗██', '║░░██║██', '║░░██║██', '████╔╝██', '════╝░╚═'),
        ('█╗░░██╗', '██╗░██║', '╔██╗██║', '║╚████║', '║░╚███║', '╝░░╚══╝'),
        ('░░██████╗░\n', '░░╚════██╗\n', '░░░█████╔╝\n', '░░░╚═══██╗\n', '░░██████╔╝\n', '░░╚═════╝░\n')]

    for part_version in range(6):
        elem = 0
        for _ in range(8):
            adjustment_version = ""
            if _ == 0 and windows_version in [8, 10]:
                adjustment_version = "\t  " * 2
            sys.stdout.write(adjustment_version + Fore.LIGHTYELLOW_EX + version[elem][part_version])
            sleep(version_seconds)
            elem += 1

    if windows_version in [8, 10]:
        print(
            "\n                          You must remember the number to be displayed." if language == 1
            else "\n                          Вы должны запомнить число которое будет выводиться на экран.")
        sleep(button_space)
    else:
        print("         If You want to change the settings of program - press the 'Space'." if language == 1
              else "      Если Вы захотите изменить настройки программы - нажмите 'Пробел'.")

    sleep(button_space)

    adjustment_information = ""
    if windows_version in [8, 10]:
        adjustment_information = "\t" * 2

    while True:
        window_counter += 1

        if window_counter == 5:
            memory_trainer_view_seconds, version_seconds, button_space = 0, 0, 0
            break
        try:
            if how_len_number is None:
                how_len_number = int(input(adjustment_information +
                                           "                   How many characters will your number include?: "
                                           if language == 1 else adjustment_information +
                                           "                Какое количество знаков будет в вашем числе?: "))
            break
        except ValueError:
            pass

    while True:
        window_counter += 1

        if window_counter >= 5:
            memory_trainer_view_seconds, version_seconds, button_space = 0, 0, 0
            break
        try:
            how_time_number = int(input(adjustment_information +
                                        "             How long will it take for memorizing numbers?: "
                                        if language == 1 else adjustment_information +
                                        "              Сколько времени потребуется на запоминание чисел?: "))
            break
        except ValueError:
            pass

# Adding numbers to the number we set earlier;
how_numbers = how_numbers.ljust(how_len_number, "0")

after_continue_random = None

cls()

# Main process of the program(Begin);
while True:

    # Generation random number;
    if after_continue_random is not None:
        random_number = after_continue_random
    else:
        random_number = randint(int(how_numbers), 9 * int(how_numbers))

    # Remember;
    print("\nRemember: " + Fore.LIGHTYELLOW_EX + str(random_number) if language == 1
          else "\nЗапомните: " + Fore.LIGHTYELLOW_EX + str(random_number))

    # Erasing the numbers written earlier in the query;
    threading.Thread(target=for_honesty, args=(how_time_number,), daemon=True).start()

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
            else "\nЕсли Вы действительно хотите закончить процесс, вот команды:\n- Если Вы хотите выйти, "
                 "нажмите пробелл; "
                 "\n- Если хотите продолжить введите число - '6'; \n- Если вы захотите изменить настройки - введите "
                 "'пар'; "
                 "\n- Если Вы хотите изменить язык программы - 'Язык'.")

        ask_exit = input(">>> ")

        # Exit from program;

        # Continue of the program;
        if ask_exit == "6":
            after_continue_random = random_number
            continue

        elif ask_exit.lower() in ["lang", "язык"]:
            change_language = None
            while True:
                try:
                    cls()
                    print("Enter number of language how you will use: \n1) English(ENG); \n2) Russian(RU)."
                          if language == 1 else "Введите номер языка который Вы хотите использовать: \n1) Английский("
                                                "ENG); \n2) Русский(RU).")

                    language = int(input(">>> "))

                    if language == 1 or 2:
                        print("Language has been changed!" if language == 1 else "Язык был изменён!")
                        sleep(1)
                        cls()
                        break

                except ValueError:
                    pass

        # Settings(Begin);
        elif ask_exit.lower() in ["set", "пар", "пар"]:

            previous_len, previous_time = how_len_number, how_time_number
            previous_len_accept, previous_time_accept = None, None

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

                            previous_time_accept = True

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
                                how_numbers = how_numbers.ljust(how_len_number, "0")
                                previous_len_accept = True

                                break
                        except ValueError:
                            continue

                # Exit from settings;
                continue_or_again = input("\nDo You want to exit the settings? [Y]es / [N]o: " if language == 1
                                          else "\nВы хотите выйти с настроек? [Д]а / [Н]ет: ").upper()

                if continue_or_again.upper() in ["Y", "Д", "Д"]:

                    if previous_time != how_time_number and previous_time_accept \
                            or previous_len != how_len_number and previous_len_accept:
                        changed_values += 1

                    break

        # Wrong command;
        if ask_exit == "":
            cls()
            write_to_file = input("Can I write your results to a file? [Y]es / [N]o: " if language == 1 else
                                  "Могу я записать ваши результаты в файл? [Д]а / [Н]ет: ")

            if write_to_file.upper() in ["Y", "Д", "Д"]:
                file_name = input("\nWrite name of file: " if language == 1 else "\nВведите имя файла: ")
                valid_files = ["pdf", "txt", "doc", "docx", "rtf"]
                while True:
                    file_format = input(
                        "Write format of file. If you want leave format by standard(.txt) press 'Enter': "
                        if language == 1 else
                        "Введите формат файла. Если хотите оставить стандартный(.txt), нажмите Пробелл: ")

                    if file_format == "":
                        file_format = "txt"

                    if not file_format.lower() in valid_files:
                        print(
                            Style.BRIGHT + "You was write format whose may not suit. Maybe problem to open, reading "
                                           "etc.\n" if language == 1 else
                            "Вам был написан формат, который может не подойти. "
                            "Могут возникнуть проблемы с открытием, чтением и т.д.")

                        continue_or_again = input(Style.BRIGHT + "Do you want to change your format? [Y]es / [N]o: "
                                                  if language == 1 else "Вы хотите изменить формат? [Д]а / [Н]ет:")

                        if continue_or_again.upper() not in ["Y", "Д", "Д"]:
                            break

                        sleep(2)
                    else:
                        break

                write_or_append = "w+"

                full_file_name = f"{file_name}.{file_format}"

                while True:
                    if full_file_name in os.listdir(os.getcwd()) and write_or_append == "w+":
                        print(
                            Style.BRIGHT + f"\nFile under name {full_file_name} is create in current directory. Select next operation:"
                                           "\n1) Delete the existing file and create a new one with different content;"
                                           "\n2) Append passwords to the end of an existing file;"
                                           "\n3) Give the file a new name." if language == 1 else
                            f"\nФайл под именем {full_file_name} уже есть в этой папке. Выберите следующую операцию: "
                            "\n1) Удалить существующий файл и создайть новый с другим содержимым;"
                            "\n2) Добавить пароли в конец существующего файла;"
                            "\n3) Дать файлу новое имя.")

                        while True:
                            try:
                                number = int(input(Style.BRIGHT + "Choose a number: " if language == 1
                                                   else "Выберите номер: "))

                                if number == 1 or 2:
                                    break
                            except TypeError:
                                pass

                        if number == 1:
                            os.remove(full_file_name)
                            print(Fore.LIGHTRED_EX + "Previous file has been deleted." if language == 1
                                  else Fore.LIGHTRED_EX + "Предыдущий файл был удалён.")
                            sleep(1)

                        elif number == 2:
                            write_or_append = "a+"
                            break

                        elif number == 3:
                            file_name = input("\nWrite name of file: " if language == 1 else "\nВведите имя файла: ")
                            full_file_name = f"{file_name}.{file_format}"

                    else:
                        break

                file = open(f"{full_file_name}", f"{write_or_append}")
                file.writelines(
                    f"\n\n{str(datetime.now())[:19].replace('-', '.')}) Successful results: {counter_True}, not quite {counter_False}."
                    f"\nChange settings: {changed_values} times. Day by day you are getting stronger.")
                file.close()
                print(Fore.LIGHTGREEN_EX + "The result file was created successfully.")
                sleep(1)

            cls()
            print(Fore.YELLOW +
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

        else:
            print("\nTry again write command!" if language == 1 else "Попробуйте ещё раз ввести команду!")
            continue

    # Question to settings and etc.(End);

    # Print of answer(Begin);
    try:
        cls()
        cls_down()
        if memorization_combo % 5 == 0:
            print(Fore.LIGHTRED_EX +
                  '                         ██████╗░░█████╗░░░██╗████████╗██╗\n'
                  '                         ██╔══██╗██╔══██╗░░██║╚══██╔══╝██║\n'
                  '                         ██║░░██║██║░░██║░░██║░░░██║░░░██║\n'
                  '                         ██║░░██║██║░░██║░░██║░░░██║░░░╚═╝\n'
                  '                         ██████╔╝╚█████╔╝░░██║░░░██║░░░██╗\n'
                  '                         ╚═════╝░░╚════╝░░░╚═╝░░░╚═╝░░░╚═╝\n')
            sleep(0.5)

        # Right answer;
        if int(how_the_number) == random_number:
            print(Fore.LIGHTGREEN_EX + congratulation[randint(1, 3)] if language == 1 else
                  Fore.LIGHTGREEN_EX + '                    ██████╗░███████╗██████╗░██╗░░██╗░█████╗░██╗\n'
                                       '                    ██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██║\n'
                                       '                    ██████╦╝█████╗░░██████╔╝███████║██║░░██║██║\n'
                                       '                    ██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║╚═╝\n'
                                       '                    ██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝██╗\n'
                                       '                    ╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝\n')

            counter_True += 1
            memorization_combo += 1

        # Wrong answer;
        else:
            print(Fore.LIGHTRED_EX +
                  '         ███╗░░██╗░█████╗░████████╗░░████████╗██████╗░██╗░░░██╗███████╗██╗\n'
                  '         ████╗░██║██╔══██╗╚══██╔══╝░░╚══██╔══╝██╔══██╗██║░░░██║██╔════╝██║\n'
                  '         ██╔██╗██║██║░░██║░░░██║░░░░░░░░██║░░░██████╔╝██║░░░██║█████╗░░██║\n'
                  '         ██║╚████║██║░░██║░░░██║░░░░░░░░██║░░░██╔══██╗██║░░░██║██╔══╝░░╚═╝\n'
                  '         ██║░╚███║╚█████╔╝░░░██║░░░░░░░░██║░░░██║░░██║╚██████╔╝███████╗██╗\n'
                  '         ╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝\n' if language == 1 else

                  Fore.LIGHTRED_EX + '          ██╗░░██╗███████╗░░██████╗░███████╗██████╗░██╗░░██╗░█████╗░██╗\n'
                                     '          ██║░░██║██╔════╝░░██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██║\n'
                                     '          ███████║█████╗░░░░██████╦╝█████╗░░██████╔╝███████║██║░░██║██║\n'
                                     '          ██╔══██║██╔══╝░░░░██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║╚═╝\n'
                                     '          ██║░░██║███████╗░░██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝██╗\n'
                                     '          ╚═╝░░╚═╝╚══════╝░░╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝\n')

            counter_False += 1

            memorization_combo = 1

        cls_down(7)
        sleep(3)

    except ValueError:
        continue

    # Answer errors or correct answer(Begin);
    decomposition_one = str(random_number).split()
    decomposition_two = how_the_number.split()

    combination = []

    counter_split = -1

    for machine in decomposition_two:
        counter_symbol = 0
        counter_split += 1
        for part_of_machine in machine:
            try:
                if part_of_machine == decomposition_one[counter_split][counter_symbol]:
                    combination.append(Fore.LIGHTGREEN_EX + decomposition_one[counter_split][counter_symbol])

                else:
                    combination.append(Fore.LIGHTRED_EX + decomposition_two[counter_split][counter_symbol])

                counter_symbol += 1

            except IndexError:
                combination.append(Fore.LIGHTRED_EX + part_of_machine)

        try:
            for i in range(len(decomposition_one[counter_split]) - len(machine)):
                combination.append(Fore.LIGHTRED_EX + "?")
        except IndexError:
            break

        combination.append(" ")

    print(Fore.LIGHTGREEN_EX + f"{'Question' if language == 1 else 'Вопрос'}: {str(random_number)}" + ' → '
          + f"{'Answer' if language == 1 else 'Ответ'}: {''.join(combination)}" + "\n")
    # Answer errors or correct answer(End);

    # Conclusion of all answers: True or False;
    print(
        Style.BRIGHT + f"{'Answers' if language == 1 else 'Ответ'}: " + (Fore.LIGHTGREEN_EX + str(counter_True)),
        "/", (Fore.LIGHTRED_EX + str(counter_False)))

    print(Style.BRIGHT + "Combo:" if language == 1 else
          Style.BRIGHT + "Комбо:", Fore.LIGHTRED_EX + "x" + str(memorization_combo))

    after_continue_random = None

    if int(how_the_number) != random_number:
        sleep(2)
# Main process of the program(End);
