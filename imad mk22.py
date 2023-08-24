import random
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
     return 0
    if 11 in cards and sum(cards)  >21:
       cards.remove(11)
       cards.append(1)
    return sum(cards)
def campare(user_score,computer_score):
    if user_score==computer_score:
        return "draw"
    elif computer_score==0:
        return "Lose, oppenent has blackjack"
    elif user_score==0:
        return "win with blackjack "
    elif user_score >  21:
        return "you went over 21 , you lost"
    elif computer_score >  21:
        return "YOU  went over , YOU LOST "
    elif user_score > computer_score:
        return "user win"
    else:
        return "you lose "
user_card=[]
computer_card=[]
is_game_over=False
for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
while not is_game_over:
    user_score=calculate_score(user_card)
    computer_score=calculate_score(computer_card)
    print(f"your card is {user_card} and current score is {user_score}")
    print(f" computer first card  is {computer_card[0]} ")
    if user_score==0 or computer_score ==0 or user_score >21:
        is_game_over=True
    else:
        user_should_deal=input("type 'y' to add another card or 'n' to pass ")
        if user_should_deal=="y":
            user_card.append(deal_card())
        else:
            is_game_over=True
while not computer_card!= 0 and computer_card < 17:
    computer_card.append(deal_card())
    computer_score=calculate_score(computer_card)
print(f" your final hand has{user_card} and final score is {user_score}")
print(f" your final hand has{computer_card} and final score is {computer_score}")
print(campare(user_score,computer_score))

