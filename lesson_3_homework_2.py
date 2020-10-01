# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def collect_info(name='Name', surname='Surname', b_year='----', city='----', email='email', phone='----'):
    """Accepts multiple parameters as arguments and returns as one string

    Optional keyword arguments:
    name = user name, default Name;
    surname = user surname, default Surname;
    b_year = user's year of birth, default ----;
    city = user's city of residence, default ----;
    email = user email, default ----;
    phone = user phone number, default ----
        """
    return f'{name.title()} {surname.title()}, born in {b_year}, lives in {city.title()},' \
           f' email: {email}, phone number: {phone}. '


if __name__ == '__main__':
    print(collect_info(name='kate',
                       surname='smith',
                       city='moscow',
                       phone='81234567890',
                       b_year=2020,
                       email='123@mail.ru'
                       )
          )
