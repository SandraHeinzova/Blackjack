import random
import os
from art import logo

def game(): 
    print(logo)
    def compare(user_score, computer_score):
          if user_score == computer_score:
              print(f"Your final hand: {user_cards}, final score {user_score}")
              print(
                  f"Computer´s final hand: {computer_cards}, final score {computer_score}"
              )
              print("It´s a draw!")
              
          elif computer_score == 0:
              print(f"Your final hand: {user_cards}, final score {user_score}")
              print(
                  f"Computer´s final hand: {computer_cards}, final score {computer_score}"
              )
              print("Oponent have a Blackjack! You lose!")
              
          elif user_score > 21:
              print(f"Your final hand: {user_cards}, final score {user_score}")
              print(
                  f"Computer´s final hand: {computer_cards}, final score {computer_score}"
              )
              print("You went over! You lose!")
             
          elif user_score == 0:
              print(f"Your final hand: {user_cards}, final score {user_score}")
              print(
                  f"Computer´s final hand: {computer_cards}, final score {computer_score}"
              )
              print("You win with Blackjack!")
              
          elif computer_score > 21:
              print(f"Your final hand: {user_cards}, final score {user_score}")
              print(
                  f"Computer´s final hand: {computer_cards}, final score {computer_score}"
              )
              print("Oponent went over! You win!")
                            
          else:
              if computer_score > user_score:
                  print(
                      f"Your final hand: {user_cards}, final score {user_score}")
                  print(
                      f"Computer´s final hand: {computer_cards}, final score {computer_score}"
                  )
                  print("You lost!")
                  
                  
              else:
                  print(
                      f"Your final hand: {user_cards}, final score {user_score}")
                  print(
                      f"Computer´s final hand: {computer_cards}, final score {computer_score}"
                  )
                  print("You win!")
  
  
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
  
    def deal_card():
          user_card = random.choice(cards)
          return user_card

    user_cards = []
    computer_cards = []
    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    
    def calculate_score(list_of_cards):
        for x in list_of_cards:
            if x == 11 and sum(list_of_cards) > 21:
                list_of_cards.remove(11)
                list_of_cards.append(1)
        score = sum(list_of_cards)
        if score == 21:
            score = 0

        return score
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, actual score: {user_score}")
    print(f"Computer first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0 or user_score > 21:
       compare(user_score, computer_score)
    else: 
           
      another_card = input("Would you like another card? Type 'y' if yes, type 'n' to pass.: ")
      if another_card == "y":
          while True:
                if computer_score == 0 or user_score == 0 or user_score > 21:
                  compare(user_score, computer_score)
                  break
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
             
                print(f"Your cards: {user_cards}, actual score: {user_score}")
                print(f"Computer first card: {computer_cards[0]}")
                if user_score > 21 or computer_score > 21 or user_score == 0:
                  compare(user_score, computer_score)
                  return False
                else:
                  another_card = input("Would you like another card? Type 'y' if yes, type 'n' to pass.: ")
      else:
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
            compare(user_score, computer_score)
  

    
    
want_play = input("Do you want to play a Blackjack? 'y' or 'n': ")
if want_play == "y":
    while True:
        os.system("cls")
        game() 
        want_play = input("Do you want to play again? Type 'y' if yes or type 'n' if no: ")
        if want_play == "n":
            print("See you next time! Bye.")  
            break            
else:
  print("Maybe next time! Bye.")    
    