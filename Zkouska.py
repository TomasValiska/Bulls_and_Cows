import time         
from random import choice

game_counts = 0
loop_counts = 0
counts = {'cow':0, 'cows':1, 'bull':0, 'bulls':1} 
statistics = {}

def not_num_analyzer(string):
  not_number = []
  for x in string:
    if not x.isnumeric():
      not_number.append(x)
  return not_number



game_counter =  True
play_is_running = True



while game_counter:
  time_start = time.time()
  game_counts += 1
  four_digit_random = []
  for x in range (1000, 10000): 
    if len(set(str(x))) == 4:
      four_digit_random.append(x)
  secret_number = choice(four_digit_random)

  print("Hi there!")
  print("-" * 47)
  print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
  print("-" * 47)
  print('Enter a number:')

    

  while play_is_running:
  
    
    print(secret_number)    
    loop_counts += 1
    
    guessed_number = input(f"-----------------------------------------------\n>>> ")
  
    if guessed_number.startswith("0") and guessed_number.isnumeric() and len(str(guessed_number)) == 4 and len(set(str(guessed_number))) == 4:
      print("Your number starts with zero.")
    elif guessed_number.startswith("0") and guessed_number.isnumeric() and len(str(guessed_number)) != 4 and len(set(str(guessed_number))) == len(str(guessed_number)):
      print("Your number starts with zero.\nYour number is not four digits.")
    elif guessed_number.startswith("0") and guessed_number.isnumeric() and len(str(guessed_number)) == 4 and len(set(str(guessed_number))) < len(str(guessed_number)):
      print("Your number starts with zero.\nYour number has repeating digits.")
    elif guessed_number.startswith("0") and guessed_number.isnumeric() and len(str(guessed_number)) != 4 and len(set(str(guessed_number))) < len(str(guessed_number)):
      print("Your number starts with zero.\nYour number is not four digits.\nYour number has repeating digits.")
    elif not_num_analyzer(guessed_number) and len(str(guessed_number)) != 4 and len(set(str(guessed_number))) < len(str(guessed_number)):
      print("The data entered are not just digits.\nThe data entered does not have four characters.\nThe data entered has repeating characters.")
    elif not_num_analyzer(guessed_number) and len(str(guessed_number)) != 4:
      print("The data entered are not just digits.\nThe data entered does not have four characters.")
    elif not_num_analyzer(guessed_number) and len(set(str(guessed_number))) < len(str(guessed_number)):
      print("The data entered are not just digits.\nThe data entered has repeating characters.")
    elif not_num_analyzer(guessed_number):
      print("The data entered are not just digits.")
    elif len(str(guessed_number)) != 4 and len(set(str(guessed_number))) < len(str(guessed_number)):
      print("Your number is not four digits.\nYour number has repeating digits.")
    elif len(str(guessed_number)) != 4:
      print("Your number is not four digits.")
    elif len(set(str(guessed_number))) != 4:
      print("Your number has repeating digits.")
    
    elif all(y not in str(secret_number) for y in guessed_number):
      print('0 bull, 0 cow')
  
    
    elif any(z in str(secret_number) for z in guessed_number) and guessed_number != str(secret_number):
      for dig in guessed_number:
        if dig in str(secret_number) and guessed_number.index(dig) != str(secret_number).index(dig) and counts['cow'] == 1:
          counts['cows'] += 1
        if dig in str(secret_number) and guessed_number.index(dig) != str(secret_number).index(dig) and counts['cow'] == 0:
          counts['cow'] += 1
        if dig in str(secret_number) and guessed_number.index(dig) == str(secret_number).index(dig) and counts['bull'] == 1:
          counts['bulls'] += 1  
        if dig in str(secret_number) and guessed_number.index(dig) == str(secret_number).index(dig) and counts['bull'] == 0:
          counts['bull'] += 1      
           
      if counts['cow'] == 1 and counts['cows'] == 1 and counts['bull'] == 1 and counts['bulls'] == 1:
        print(f"bull {counts['bull']}, cow {counts['cow']}")
      elif counts['cow'] == 0 and counts['cows'] == 1 and counts['bull'] == 1 and counts['bulls'] == 1:
        print(f"bull {counts['bull']}, cow {counts['cow']}")
      elif counts['cow'] == 1 and counts['cows'] == 1 and counts['bull'] == 0 and counts['bulls'] == 1:
        print(f"bull {counts['bull']}, cow {counts['cow']}")
      elif counts['cow'] == 1 and counts['cows'] == 1 and counts['bull'] == 1 and counts['bulls'] > 1:
        print(f"bulls {counts['bulls']}, cow {counts['cow']}")
      elif counts['cow'] == 1 and counts['cows'] > 1 and counts['bull'] == 1 and counts['bulls'] == 1:
        print(f"bull {counts['bull']}, cows {counts['cows']}")
      elif counts['cow'] == 0 and counts['cows'] == 1 and counts['bull'] == 1 and counts['bulls'] > 1:
        print(f"bulls {counts['bulls']}, cow {counts['cow']}")
      elif counts['cow'] == 1 and counts['cows'] > 1 and counts['bull'] == 0 and counts['bulls'] == 1:
        print(f"bull {counts['bull']}, cows {counts['cows']}")
      else:
        print(f"bulls {counts['bulls']}, cows {counts['cows']}")
    

   
      counts.update({'cow':0})
      counts.update({'cows':1})
      counts.update({'bull':0})
      counts.update({'bulls':1})
      continue

    elif guessed_number == str(secret_number):
      if loop_counts == 1:
        print(f"Correct, you've guessed the right number \nin {loop_counts} guess!")
        print("-" * 47)
      else:
        print(f"Correct, you've guessed the right number \nin {loop_counts} guesses!")
        print("-" * 47)
      if loop_counts <= 4:
        print('That is amazing!')
      elif loop_counts >= 5 and loop_counts <= 9:
        print("That is average.")
      else:
        print("That is not so good.")
      play_is_running =  False
      


  time_end = time.time()
  duration = time_end - time_start
  
  
  print(f"The game lasted {round(duration)} seconds.")
  add_to_statistics = {"game duration":round(duration), "number of guesses":loop_counts}
  statistics[game_counts] = add_to_statistics
  loop_counts = 0
  exit = input("To exit the game, type 'end'. To continue, type any other character. ")
  print()
  if exit == "end":
    game_counter = False
  else:
    play_is_running = True
  
  continue

print("-" * 47)
print("{:3}|{:^9}|{:>18}".format("GAME NUMBER  ", "  DURATION  ", "NUMBER OF GUESSES"))
print("-" * 47)

for key, value in statistics.items():
    print("{:>6}".format(key), "      |", end=" ")
    for index, v in enumerate(value.values()):
        print("{:>5}".format(v), end=" ")
        if index != len(value.values()) - 1:
            print("     |", end=" ")
        
    print()