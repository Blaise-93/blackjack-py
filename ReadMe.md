# Blackjack Game
A blackjack game  written in python which you can play and determine whether you win or lose.
Here, we have 52 cards and all cards can be exhausted between the player and the dealer, provided 
that we have a winner. The players can actually terminate the game halfway and a winner might still
be emerged depending on the card each of the player is currtently holding. 
The `check_winner` method of `Game class` actually does that for us with while loop functionality in 
our scripts. If there is no winner, the game will continue till by prompting you to select
Hit or Stand till we have a winner. For example, when the two 
players are holding a blackjack, of course, it is a tie. The game goes on. :D

#### Code snippet of what happens behind the scene:

```python`

    def check_winner(self, dealer_hand, player_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You bursted, dealer win! ☕")
                return True

            elif dealer_hand.get_value() > 21:
                print("Dealer bursted. You win! ❤️")
                return True

            elif dealer_hand.is_blackjack() and \
                    player_hand.is_blackjack():
                print("Both players have blackjack! Tie ")
                return True

            elif player_hand.is_blackjack():
                print("You have a blackjack. You win! ❤️")
                return True

            elif dealer_hand.is_blackjack():
                print("Dealer have a blackjack. Dealer Wins. You are bursted, dude! ")
                return True

        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print('You win! ❤️')

            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a Tie")

            else:
                print('Dealer win! ')

            return True
        return False


``
-- Pictorial Reprensentation of the game in your terminal:
![blackjack-py](https://github.com/Blaise-93/blackjack-py/assets/58372011/b14d2035-055c-4e4a-9e16-29f9d42cee44)

To play this amazing game all you need to do is to clone this in your terminal:

```shell
  git@github.com:Blaise-93/blackjack-py.git
```

- and then you can play the game.

Thanks for checking out, goodluck!
