suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
n=input().split()
for i in n:
    card_value = int(i)
    suit_value = int(card_value / 13)
    rank_value = card_value % 13
    for ind in suits:
        if suit_value==suits.index(ind): #comparison with index lists
            suit_value=ind
    for ind in ranks:
        if rank_value==ranks.index(ind):
            rank_value=ind
    print(rank_value+'-of-'+ suit_value, end=' ')
