def ask_data ():
    s_name = input ('Введите фамилию: ')
    f_name = input ('Введите имя: ')
    m_name = input ('Введите отчество: ')
    phone = input ('Введите номер телефона: ')
    contact = {'second_name': s_name, 'first_name': f_name, 'middle_name': m_name, 'phone_number': phone}
    return contact

def add_new_contact ():
    contact = ask_data ()
    with open ('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values ():
            file.write (f'{value}; ')
        file.write ("\n")# нельзя делать такие же кавычки, как в основном тексте
    return True

def open_phonebook ():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        print ("\t\t".join(title))# пишем разделитель перед join (эта функция только для списков)
        for line in file:
            print ("\t\t".join(line.split(';')))
            
def find_contact ():
    title = ["Фамилия", "Имя", "Отчество", "Телефон"]
    s_name = input ("Введите фамилию: ")
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        print ("\t\t".join(title))
        for line in file:
            line = line.split (";")
            if s_name == line [0]:
                print ('\t\t'.join (line))
                
def delete_contact ():
    s_name = input ("Введите фамилию: ")
    lines = []
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines ()# сделали из lines список, состоящий из строк файла ['иванов; иван; иванович; 09790', 'сошкина; алина; андреевна; 98790']
    with open ('phonebook.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            if s_name not in line:
                file.write (line)

def copy_contact ():
    num = int (input ('Введите номер строки: '))
    list_1 = []
    with open ('phonebook.txt', 'r', encoding='utf-8') as file:
        list_1 = file.readlines ()
    with open ('new_phonebook.txt', 'w', encoding='utf-8') as nfile:
        for number, line in enumerate (list_1):
            if number == num:
                nfile.write (line)

def main ():
    flag = 1
    while flag != 0:
        print ('Введите, что хотите сделать:\n1 найти\n2 добавить\n3 удалить\n4 открыть\n5 копировать\n0 выход')
        flag = int (input ('>>'))
        if flag == 1:
            find_contact ()
        elif flag == 2:
            add_new_contact ()
        elif flag == 3:
            delete_contact ()
        elif flag == 4:
            open_phonebook ()
        elif flag == 5:
            copy_contact ()
        input ('Нажмите enter, чтобы продолжить')

main()