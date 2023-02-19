"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений. 
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3$. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4$. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5$. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list({random.randint(1, 10000) for _ in range(random.randint(5, 20))})
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice([None, random.choice([m["id"] for m in messages]) if messages else []]),
            "seen_by": random.sample(users_ids, random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


def user_messages(messages): # 'id пользователя: список с id всех его сообщений
    user_messages = {}
    for _ in messages:
        sender_id = _['sent_by']
        message_id = _['id']
        
        if user_messages.get(sender_id) == None:
            user_messages[sender_id] = [message_id]
        else:
            user_messages[sender_id].append(message_id)
    return user_messages # 'id пользователя: список с id всех его сообщений
def first_issue(user_messages):
    wrote_the_most = max(user_messages.values(), key=len)
    for _ in user_messages:
        if user_messages[_] == wrote_the_most:
            wrote_the_most = _
    return wrote_the_most


def number_answers(messages):
    number_answers = {}
    for _ in messages:
        if _['reply_for'] != None and _['reply_for'] != []:
            if _['reply_for'] in number_answers:
                number_answers[_['reply_for']] += 1
            else:
                number_answers[_['reply_for']] = 1
    return number_answers
def second_issue(number_answers):
    number_responses_per_user = {}
    for _ in chat_history:
        message_id = _['id']
        for i in number_answers:
            if i == message_id:
                if number_responses_per_user.get(_['sent_by']) == None:
                    number_responses_per_user[_['sent_by']] = number_answers[i]
                else:
                    number_responses_per_user[_['sent_by']] += number_answers[i]
    most_cited = max(number_responses_per_user.values())
    for _ in number_responses_per_user:
        if number_responses_per_user[_] == most_cited:
            most_cited = _
    return most_cited


def how_many_views(user_messages):
    how_many_views = {}
    reply = []
    for _ in user_messages:
        who_saw = []
        message_list = user_messages[_]
        for i in message_list:
            for j in chat_history:
                if j['id'] == i:
                    who_saw += j['seen_by']
        how_many_views[_] = len(who_saw)
    most_viewed = max(how_many_views.values())
    for _ in how_many_views:
        if how_many_views[_] == most_viewed:
            reply.append(_)
    return reply


def sending_time(messages):
    sending_time = {
        'morning': 0,
        'day': 0,
        'evening': 0,
        'night': 0
    }
    for _ in messages:
        time = int(_['sent_at'].strftime('%H'))
        if 6 <= time < 12:
            sending_time['morning'] += 1
        elif 12 <= time < 18:
            sending_time['day'] += 1
        elif 18 <= time < 23:
            sending_time['evening'] += 1
        else:
            sending_time['night'] += 1
    busiest_time = max(sending_time.values())
    for _ in sending_time:
        if sending_time[_] == busiest_time:
            return _


def is_there_answer(id):
    for _ in chat_history:
        if _['reply_for'] == id:
            return True
    return False
def reply_for_from_id(id):
    for _ in chat_history:
        if _['id'] == id:
            return _['reply_for']
def message_threads(messages):
    message_threads = {}
    reply = []
    for _ in messages:
        answer = is_there_answer(_['id'])
        count = 0
        by = _['id']
        beginning = _['reply_for']
        if answer == False:
            while beginning != None and beginning != []:
                by = beginning
                beginning = reply_for_from_id(beginning)
                count += 1
        if count > 0:
            message_threads[by] = count
    
    max_branch_length = max(message_threads.values())

    for _ in message_threads:
        if message_threads[_] == max_branch_length:
            reply.append(_)
    return reply


if __name__ == "__main__":
    chat_history = generate_chat_history()

    print(f'ID пользователя, который написал больше всех сообщений: {first_issue(user_messages(chat_history))}', end='\n\n')

    print(f'ID пользователя, на которого больше всего отвечали: {second_issue(number_answers(chat_history))}', end='\n\n') #2

    print('ID пользователя с наибольшим кол-ом просмотров:', end=' ') #3
    print(*how_many_views(user_messages(chat_history)), end='\n\n')

    print(f'Больше всего сообщений: {sending_time(chat_history)}', end='\n\n') #4

    print('Начало для самых длинных тредов:', end='\n') #5
    print(*message_threads(chat_history), sep='\n') 