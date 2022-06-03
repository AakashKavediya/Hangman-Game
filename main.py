def play():
  from wordfile import words
  import random
  return random.choice(words)

a = play()
a = list(a)
print("You have to guess your word : ")
print("_ "*len(a))
answer=("_"*len(a))
answer=list(answer)
while True:
  if answer == a:
    print('You won the game.')
    break
  b = input("Enter the guess: ")
  if b in a:
    for i in range(len(a)):
      if a[i] == b:
        answer[i] = b
        print ("Your guess is  right: ")
        print(" ".join(answer))
  else:
   print("wrong guess, Try again:")


