users = []

user = {}

user['imie'] = input('Podaj nazwę użytkownika: ')
user['email'] = input('Podaj email użytkownika: ')

users.append(user)

print(f'Użytkownik {user} został dodany do bazy danych')

print('Wszyscy użytkownicy: ')
for u in users:
    print(f'Użytkownik: {u}')
