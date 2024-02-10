class Student:
    def __init__(self, name, surname, classroom):
        self.name = name
        self.surname = surname
        self.classroom = classroom

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.classroom}"

    def is_student_found(self, name, surname):
        return self.name == name and self.surname == surname

    def is_classroom(self, classroom):
        return self.classroom == classroom


class Teacher:
    def __init__(self, name, surname, classroom, subject):
        self.name = name
        self.surname = surname
        self.classroom = classroom
        self.subject = subject

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.classroom} {self.subject}"

    def is_teacher_found(self, name, surname):
        return self.name == name and self.surname == surname


class Master:
    def __init__(self, name, surname, classroom):
        self.name = name
        self.surname = surname
        self.classroom = classroom

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.classroom}"

    def is_head_teacher_found(self, name, surname):
        return self.name == name and self.surname == surname


students_list = []
teachers_list = []
head_teachers_list = []
classroom = []

students_list.append(Student("Jan", "Kowalski", "3C"))  # TODO Do usuniecia pozniej
students_list.append(Student("Tomasz", "Jankowski", "5E"))  # TODO Do usuniecia pozniej
students_list.append(Student("Marek", "Nowak", "5E"))  # TODO Do usuniecia pozniej
teachers_list.append(Teacher("Marek", "Nowak", "3C", "Historia"))  # TODO Do usuniecia pozniej
teachers_list.append(Teacher("Bartosz", "Janiak", ["3C", "4D", "5E"], "Matematyka"))  # TODO Do usuniecia pozniej
head_teachers_list.append(Master("Mietek", "Szcześniak", "3C"))  # TODO Do usuniecia pozniej
head_teachers_list.append(Master("Andrzej", "Mata", "5E"))  # TODO Do usuniecia pozniej


while True:
    command = input("Podaj polecenie (utworz/zarzadzaj/koniec): ").title()
    if command == "Utworz":
        print("Proces tworzenia użytkownika")
        while True:

            create_input = input("Podaj komendę (uczen/nauczyciel/wychowawca/koniec): ").title()
            if create_input == "Uczen":
                print("Proces tworzenia ucznia")
                name = input("Podaj imię ucznia: ").title()
                if not name:
                    print("Uczeń nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko ucznia: ").title()
                if not surname:
                    print("Uczeń nie może mieć pustego nazwiska!")
                    continue
                classroom = input("Podaj klasę ucznia: ").title()
                if not classroom:
                    print("Uczeń nie może nie być przypisany do klasy!")
                    continue
                students_list.append(Student(name, surname, classroom))

            elif create_input == "Nauczyciel":
                print("Proces tworzenia nauczyciela")
                name = input("Podaj imię nauczyciela: ").title()
                if not name:
                    print("Nauczyciel nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko nauczyciela: ").title()
                if not surname:
                    print("Nauczyciel nie może mieć pustego nazwiska!")
                    continue

                subject = input("Podaj przedmiot nauczyciela: ").title()
                if not subject:
                    print("Nauczyciel nie może nie mieć przedmiotu!")
                    continue

                while True:
                    classrooms = input("Podaj klasę nauczyciela: ").title()
                    if not classrooms:
                        break
                    else:
                        classroom.append(classrooms)
                teachers_list.append(Teacher(name, surname, classroom, subject))

            elif create_input == "Wychowawca":
                print("Proces tworzenia wychowawcy")
                name = input("Podaj imię wychowawcy: ").title()
                if not name:
                    print("Wychowawca nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko wychowawcy: ").title()
                if not surname:
                    print("Wychowawca nie może mieć pustego nazwiska!")
                    continue
                classroom = input("Podaj klasę wychowawcy: ").title()
                if not classroom:
                    print("Wychowawca nie może nie być przypisany do klasy!")
                    continue
                head_teachers_list.append(Master(name, surname, classroom))

            elif create_input == "Koniec":
                print("Opuszczam proces tworzenia")
                break
            else:
                print(f"Podano błędną komendę: {create_input}")

    elif command == "Zarzadzaj":
        print("Proces zarzadzania")

        while True:

            manage_input = input("Wprowadź komendę (klasa, uczen, nauczyciel, wychowawca, koniec)").title()

            if manage_input == "Uczen":
                print("Proces zadządzania uczniem")
                name = input("Podaj imię ucznia: ").title()
                if not name:
                    print("Uczeń nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko ucznia: ").title()
                if not surname:
                    print("Uczeń nie może mieć pustego imienia!")
                    continue

                student_found = None
                teacher_found = None

                for single_student in students_list:  # iterujemy po liście studentów
                    if single_student.is_student_found(name, surname):
                        print(f"Znaleziono ucznia: {single_student}")
                        student_found = single_student
                        break

                if student_found:
                    find_classroom = student_found.classroom
                    print(f"Uczeń chodzi na lekcje: ")
                    for single_teacher in teachers_list:
                        if find_classroom in single_teacher.classroom:
                            print(f"{single_teacher.subject}, którą prowadzi {single_teacher.name} "
                                  f"{single_teacher.surname}")

            elif manage_input == "Klasa":
                print("Proces zadządzania Klasą")
                classroom = input("Podaj klasę: ")
                if not classroom:
                    print("Pole nie może być puste!")
                    continue
                classroom_found = None

                for single_class in students_list:
                    if single_class.is_classroom(classroom):
                        print(f"Znaleziono klase: {single_class.classroom}")
                        classroom_found = single_class.classroom
                        break

                if classroom_found:
                    print(f"Uczniowie należący do tej klasy to: ")
                    for single_student in students_list:
                        if classroom_found in single_student.classroom:
                            print(f"{single_student.name} {single_student.surname}")

                    for single_teacher in head_teachers_list:
                        if classroom_found in single_teacher.classroom:
                            print(f"Wychowawca prowadzący tą klasę to: {single_teacher.name} {single_teacher.surname}")
                else:
                    print("Nie znaleziono klasy.")
                    continue

            elif manage_input == "Nauczyciel":
                print("Proces zadządzania Nauczycielem")
                name = input("Podaj imię Nauczyciela: ").title()
                if not name:
                    print("Nauczyciel nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko Nauczyciela: ").title()
                if not surname:
                    print("Nauczyciel nie może mieć pustego nazwiska!")
                    continue
                teacher_found = None
                for single_teacher in teachers_list:
                    if single_teacher.is_teacher_found(name, surname):
                        print(f"Znaleziono Nauczyciela: {single_teacher.name} {single_teacher.surname}")
                        teacher_found = single_teacher
                        break
                if teacher_found:
                    print(f"Prowadzi klasy {teacher_found.classroom}")

            elif manage_input == "Wychowawca":
                print("Proces zadządzania Wychowawca")
                name = input("Podaj imię Wychowawcy: ").title()
                if not name:
                    print("Wychowawca nie może mieć pustego imienia!")
                    continue
                surname = input("Podaj nazwisko Wychowawcy: ").title()
                if not surname:
                    print("Wychowawca nie może mieć pustego nazwiska!")
                    continue
                head_teacher_found = None
                for head_teacher in head_teachers_list:
                    if head_teacher.is_head_teacher_found(name, surname):
                        print(f"Znaleziono Wychowawce: {head_teacher.name} {head_teacher.surname}")
                        head_teacher_found = head_teacher
                        break

                if head_teacher_found:
                    print(f"Wychowawca prowadzi uczniów:")
                    find_classroom = head_teacher_found.classroom
                    for single_student in students_list:
                        if find_classroom in single_student.classroom:
                            print(f"{single_student.name} {single_student.surname}")

            elif manage_input == "Koniec":
                print("Opuszczam proces zarządzania")
                break

            else:
                print(f"Podano błędną komendę: {manage_input}")

    elif command == "Koniec":
        print("Koniec działania programu")
        break
    else:
        print(f"Została podana błędna komenda: {command}")
