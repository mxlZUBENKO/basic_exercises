# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(len(word))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
count = 0
for letter in word:
    if letter.lower() in vowels:
        count += 1
print(count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
count_words = len(sentence.split())
count_letters = 0
for word in sentence.split():
    count_letters += len(word)
average_length = count_letters / count_words
print(average_length)