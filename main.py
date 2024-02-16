from art import logo
import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "  Draw!"
  elif computer_score == 0:
    return "  Computer wins!"
  elif user_score == 0:
    return "  You win!"
  elif computer_score > 21:
    return "  You win!"
  elif user_score > 21:
    return "  Computer wins!"
  elif user_score > computer_score:
      return "  You win!"
  else:
      return "  Computer wins!"

def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game_over = False
  
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  user_score = 0
  computer_score = 0
  
  while not game_over:
  
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if computer_score == 0 or user_score == 0:
      game_over = True
    elif computer_score > 21 or user_score > 21:
      game_over = True
    else:
      next_card = input("Would you like to draw another card? Type 'y' or 'n': ")
      if next_card == "y":
        user_cards.append(deal_card())
      else: 
        game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
else: 
  print("Game over.")
    
    