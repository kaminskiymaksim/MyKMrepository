from random import shuffle
# Кол-во попыток.
turns = 5

print(f"Привет, Давай сыграем в виселицу! У тебя есть {turns} попыток!")
print("Отгадываем языки программирования!")
wordList = ["java", "php", "python"]
# Список слов, которые участвуют в игре.

shuffle(wordList)

word = wordList.pop()
# Берем последнее слово из списка
guesses = ""

# Цикл, который будет работать, пока не останется попыток или не отгаданных букв.
while turns > 0:
   wrong = 0

   for char in word:
       if char in guesses:
           print(char, end=" ")
       else:
           print("_", end=" ")
           wrong += 1

   print("\n")

   if wrong == 0:
       print("Ты выиграл! :)")

       break

   print()

   guess = ""
   if len(guess) < 1:
       guess = input("Впиши букву и нажми enter: ")[0]

   if guess in guesses:
       print("Эта буква уже была!")
   guesses += guess

   if guess not in word:
       turns -= 1

       print("Упс! Ошибка")
       print(f"У тебя осталось {turns} попыток")

       if turns == 0:
           print("Ты проиграл! :(")