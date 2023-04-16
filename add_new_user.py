users = []

user = input('Podaj nazwę użytkownika: ')

users.append(user)

print(f'Użytkownik {user} został dodany do bazy danych')

print('Wszyscy użytkownicy: ')
for u in users:
    print(f'Użytkownik: {u}')
