import arcade

screen_width = 1024
screen_height = 768
screen_title = "Game_Interface"


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Slot:
    def __init__(self, position, slot_type):
        self.position = position
        self.slot_type = slot_type
        self.cards = []


class Solitaire(arcade.Window):

    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.color.AMAZON)

        # Define Klondike slots
        self.tableau_slots = [Slot((screen_width - 130 * (i+1), 430), "tableau") for i in range(7)]
        self.foundation_slots = [Slot((screen_width - 130 * (i + 1), 630), "foundation") for i in range(4)]
        self.waste_pile = Slot((130, 630), "waste")

        self.card_back_texture = arcade.load_texture("CardBack.png")

    def setup(self):
        # Initialize the game state here (if needed)
        pass

    def on_draw(self):
        self.clear()

        # Draw the slots
        self.draw_slots()

    def draw_slots(self):
        # Draw tableau slots
        for slot in self.tableau_slots:
            arcade.draw_texture_rectangle(slot.position[0], slot.position[1], 85, 120, self.card_back_texture)

        # Draw foundation slots
        for slot in self.foundation_slots:
            arcade.draw_rectangle_outline(slot.position[0], slot.position[1], 85, 120, arcade.color.ASPARAGUS, border_width=5)

        # Draw waste pile slot
        arcade.draw_texture_rectangle(self.waste_pile.position[0], self.waste_pile.position[1], 85, 120, self.card_back_texture)


def main():
    window = Solitaire()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
