import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 60, 90
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load Card Images
card_images = {}
suits = ['hearts', 'spades', 'clubs', 'diamonds']
for suit in suits:
    card_images[suit] = {}
    for value in range(2, 15):
        filename = f'{value}_of_{suit}.png'
        card_images[suit][value] = pygame.image.load(os.path.join(suit, filename))

# Create Player Class
class Player:
    def __init__(self, name, assigned_suit):
        self.name = name
        self.assigned_suit = assigned_suit
        self.hand = []
        self.used_cards = []

    def deal_hand(self, deck):
        self.hand = [card for card in deck if card[1] == self.assigned_suit]

    def bid(self, diamond_card):
        available_cards = [card for card in self.hand if card not in self.used_cards]
        return random.choice(available_cards)

# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Diamond Bidding Game")

# Font
font = pygame.font.Font(None, 36)

# Main Function
def main():
    clock = pygame.time.Clock()
    running = True

    # Game Variables
    round_num = 1
    deck = [(value, suit) for value in range(2, 15) for suit in ['hearts', 'spades', 'clubs', 'diamonds']]
    random.shuffle(deck)
    player1 = Player("Player 1", "spades")
    player2 = Player("Computer", "hearts")
    player1.deal_hand(deck)
    player2.deal_hand(deck)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Press space to bid
                    player1_bid = player1.bid(deck[round_num - 1][0])
                    print(f"{player1.name} bids: {player1_bid}")
                    player2_bid = player2.bid(deck[round_num - 1][0])
                    print(f"{player2.name} bids: {player2_bid}")

        if not running:
            break  # Exit the loop if running is set to False

        screen.fill(WHITE)

        # Display Player's Hand
        x, y = 50, HEIGHT - CARD_HEIGHT - 20
        for card in player1.hand:
            suit = card[1]
            value = card[0]
            card_img = card_images[suit][value]
            screen.blit(card_img, (x, y))
            x += CARD_WIDTH + 10

        # Display Bidding Card
        bidding_card = deck[round_num - 1]
        suit = bidding_card[1]
        value = bidding_card[0]
        card_img = card_images[suit][value]
        screen.blit(card_img, (WIDTH // 2 - CARD_WIDTH // 2, HEIGHT // 2 - CARD_HEIGHT // 2))

        # Display Scoreboard
        text_round = font.render(f"Round: {round_num}", True, BLACK)
        screen.blit(text_round, (WIDTH - 150, 20))

        pygame.display.flip()
        clock.tick(30)  # Ensure smooth frame rate

        # Increase Round Number
        round_num += 1

        # Check if all rounds are completed
        if round_num > 13:
            running = False  # End the game loop

    pygame.quit()  # Quit Pygame

if __name__ == "__main__":
    main()
