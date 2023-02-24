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


def user_messages(messages):
    user_messages = {}
    for message in messages:
        sender_id = message['sent_by']
        message_id = message['id']
        
        if user_messages.get(sender_id) is None:
            user_messages[sender_id] = [message_id]
        else:
            user_messages[sender_id].append(message_id)
    return user_messages # id пользователя: id всех сообщеня
def who_wrote_the_most_posts(user_messages):
    maximum_number_of_messages = max(user_messages.values(), key=len)
    for user_id in user_messages:
        if user_messages[user_id] == maximum_number_of_messages:
            return user_id


def number_of_responses_per_message(messages):
    number_answers = {}
    for message in messages:
        if message['reply_for'] is not None and message['reply_for']:
            number_answers[message['reply_for']] = number_answers.get(message['reply_for'], 0) + 1
    return number_answers
def got_the_most_responses(number_answers):
    number_responses_per_user = {}
    for message in chat_history:
        for message_id in number_answers:
            if message_id == message['id']:
                number_responses_per_user[message['sent_by']] = number_responses_per_user.get(message['sent_by'], 0) + 1
    most_cited = max(number_responses_per_user.values())
    for uder_id in number_responses_per_user:
        if number_responses_per_user[uder_id] == most_cited:
            return uder_id


def how_many_views(user_messages):
    how_many_views = {}
    for user_id in user_messages:
        who_saw = []
        message_list = user_messages[user_id]
        for user_message in message_list:
            for message in chat_history:
                if message['id'] == user_messages:
                    who_saw += message['seen_by']
        how_many_views[user_id] = len(who_saw)
    most_viewed = max(how_many_views.values())
    for user_id in how_many_views:
        if how_many_views[user_id] == most_viewed:
            return user_id


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
    for time in sending_time:
        if sending_time[time] == busiest_time:
            return time


def is_there_answer(id):
    for message in chat_history:
        if message['reply_for'] == id:
            return True
    return False
def reply_for_from_id(id):
    for message in chat_history:
        if message['id'] == id:
            return message['reply_for']
def message_threads(messages):
    message_threads = {}
    for message in messages:
        answer = is_there_answer(message['id'])
        count = 0
        by = message['id']
        beginning = message['reply_for']
        if answer == False:
            while beginning is not None and beginning:
                by = beginning
                beginning = reply_for_from_id(beginning)
                count += 1
        if count > 0:
            message_threads[by] = count
    
    max_branch_length = max(message_threads.values())

    for message_id in message_threads:
        if message_threads[message_id] == max_branch_length:
            return message_id


if __name__ == "__main__":
    chat_history = generate_chat_history()

    print(f'ID пользователя, который написал больше всех сообщений: {who_wrote_the_most_posts(user_messages(chat_history))}', end='\n\n') #1

    print(f'ID пользователя, на которого больше всего отвечали: {got_the_most_responses(number_of_responses_per_message(chat_history))}', end='\n\n') #2

    print(f'ID пользователя с наибольшим кол-ом просмотров: {how_many_views(user_messages(chat_history))}', end='\n\n') #3

    print(f'Больше всего сообщений: {sending_time(chat_history)}', end='\n\n') #4

    print(f'Начало для самых длинных тредов: {message_threads(chat_history)}') #5