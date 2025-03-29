from requests import post

print(post('http://localhost:5000/api/jobs', json={}).json())  # нет аргументов
print(post('http://localhost:5000/api/jobs', json={
    'title': 'Заголовок',
    'content': 'Текст новости',
    'user_id': 1, }).json())  # неправильные ключи
print(post('http://localhost:5000/api/jobs', json={
    'team_leader': 1,
    'job': 'fllfflfl',
    'work_size': 1,
    'content': 111111111111111111111111111111111,
    'collaborators': 333333333333333333333333333333333333333333333333333333,
    'end_date': '26.02.2000',
    'is_finished': True}).json()) # неправильный тип данных у аргументов

print(post('http://localhost:5000/api/jobs', json={
    'team_leader': 1,
    'job': 'fllfflfl',
    'work_size': 1,
    'content': '1, 2',
    'collaborators': '1',
    'end_date': '26.02.2000',
    'is_finished': True}).json())

