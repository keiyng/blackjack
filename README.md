Blackjack with Python
==================================

A fork of https://github.com/nachogentile/learn-python-with-blackjack 's functional implementation of Blackjack (blackjack.py)

Major changes:
* each player is dealt with two initial cards without being prompted,
* players take turn to play,
* keep track of stand count to terminate the game:
```python
        if 'Player 1' in stand_count and 'Player 2' in stand_count:
            if player1_score > player2_score:
                winner = 'Player 1'
                print('%s is the winner!' % winner)
            elif player2_score > player1_score:
                winner = 'Player 2'
                print('%s is the winner!' % winner)
            else:
                print('It\'s a draw!')
                winner = 'nobody'
``` 
or to skip prompting a player who chose "stand":
```python
for player in players:
    if player in stand_count:
        continue
```


To run the script on console:
`$ python blackjack.py`
