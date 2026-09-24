import json

blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)
print(type(decoded_hand)) # <class 'list'>
print(decoded_hand) # [8, 'Q']
print(blackjack_hand == tuple(decoded_hand)) # True because they content the same values
