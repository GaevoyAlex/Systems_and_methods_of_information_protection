# импортируем необходимые модули
import random
import string
import math
import matplotlib.pyplot as plt
import numpy as np

# определяем функцию для генерации строки с заданной длиной, состоящей из символов алфавита Латиница строчные и прописные
def generate_string(length):
  # length is an integer that specifies the desired length of the string
  # returns a random string of the given length, consisting of upper and lower case letters
  alphabet = string.ascii_letters # a string containing all upper and lower case letters
  result = "" # an empty string to store the result
  for i in range(length): # loop for the given length
    result += random.choice(alphabet) # append a random letter to the result
  return result # return the result

# определяем функцию для проверки равномерности распределения символов путем визуализации частотного распределения
def plot_frequency_distribution(string):

  frequency = {} # an empty dictionary to store the frequency of each character
  for char in string: # loop through each character in the string
    if char in frequency: # if the character is already in the dictionary
      frequency[char] += 1 # increment its frequency by one
    else: # otherwise
      frequency[char] = 1 # initialize its frequency to one
  plt.bar(frequency.keys(), frequency.values()) # plot a bar chart with the keys and values of the dictionary
  plt.xlabel("Character") # label the x-axis as "Character"
  plt.ylabel("Frequency") # label the y-axis as "Frequency"
  plt.title("Frequency Distribution of Characters in " + string) # give a title to the plot
  plt.show() # show the plot

# определяем функцию для вычисления среднего времени подбора пароля, выбираемого из сгенерированной строки
def estimate_password_time(string):
  # string is a string from which a password is chosen
  # returns an estimate of the average time (in seconds) to guess a password from the string, assuming a brute force attack with one billion guesses per second
  password_length = len(string) # get the length of the password
  alphabet_size = len(set(string)) # get the size of the alphabet (the number of unique characters in the string)
  possible_passwords = alphabet_size ** password_length # calculate the number of possible passwords from the string
  average_time = possible_passwords / (2 * 10**9) # estimate the average time by dividing the number of possible passwords by twice the number of guesses per second (assuming that on average, half of the passwords are tried before finding the correct one)
  return average_time # return the estimate

# определяем функцию для построения графика зависимости среднего времени подбора пароля от его длины
def plot_password_time(string):
  # string is a string from which passwords are chosen
  # plots a line chart of the average time to guess a password from the string versus its length, assuming a brute force attack with one billion guesses per second
  alphabet_size = len(set(string)) # get the size of the alphabet (the number of unique characters in the string)
  lengths = np.arange(1, len(string) + 1) # create an array of possible lengths from one to the length of the string
  times = [estimate_password_time(string[:l]) for l in lengths] # create an array of estimated times for each length by slicing the string and calling estimate_password_time function
  plt.plot(lengths, times) # plot a line chart with lengths and times arrays
  plt.xlabel("Password Length") # label the x-axis as "Password Length"
  plt.ylabel("Average Time to Guess (seconds)") # label the y-axis as "Average Time to Guess (seconds)"
  plt.title("Average Time to Guess a Password from " + string) # give a title to the plot
  plt.show() # show the plot

# запрашиваем у пользователя желаемую длину строки
length = int(input("Введите желаемую длину строки: "))

# генерируем строку с заданной длиной, состоящей из символов алфавита Латиница строчные и прописные
string = generate_string(length)

# выводим сгенерированную строку на экран
print("Сгенерированная строка: " + string)

# проверяем равномерность распределения символов путем визуализации частотного распределения
plot_frequency_distribution(string)

# вычисляем среднее время подбора пароля, выбираемого из сгенерированной строки
time = estimate_password_time(string)

# выводим оценку среднего времени подбора пароля на экран
print("Оценка среднего времени подбора пароля из сгенерированной строки: " + str(time) + " секунд")

# строим график зависимости среднего времени подбора пароля от его длины
plot_password_time(string)
