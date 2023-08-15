# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
import random
from replit import clear

def deal_card():
  """returns a random card from a deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
def calculate_score(cards):
  if sum==21 and len(cards)==2:
    return 0

  if 11in cards and sum(cards) >21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw"
  elif user_score==0:
    return "Win with a blackjack"
  elif computer_score==0:
    return "Lose,opponent has blackjack"
  elif user_score>21:
    return "You went over.You lose!"
  elif computer_score>21:
    return "Opponent went over.You win!"
  elif user_score==computer_score:
    return "You win!"
  else:
    return "You lose"
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  is_gameover=False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while(not is_gameover):
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score} ")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      is_gameover=True
    else:
      user_deal=input("type y to add another card or n to pass: ")
      if user_deal=='y':
        user_cards.append(deal_card())
      else:
        is_gameover=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  print(compare(user_score,computer_score))
  

while input("Do you want to play a game? Type y or no:")=='y':
  clear()
  play_game()
  
