import arcade

screen_width = 1024
screen_height = 768
screen_title = "Game_Interface"
tableau_offset = 20


class Card:
    def __init__(self, tableau_position=None):
        self.tableau_position = tableau_position


class Slot:
    def __init__(self, position, slot_type):
        self.position = position
        self.slot_type = slot_type
        self.cards = []


class Solitaire(arcade.Window):

    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)

        arcade.set_background_color(arcade.color.AMAZON)

        self.tableau_slots = [Slot((screen_width - 130 * (i+1), 430), "tableau") for i in range(7)]
        self.foundation_slots = [Slot((screen_width - 130 * (i + 1), 630), "foundation") for i in range(4)]
        self.waste_pile = Slot((130, 630), "waste")

        self.card_back_texture = arcade.load_texture("cards/CardBack.png")

        self.setup()

    def setup(self):
        # Initialize the game state here (if needed)
        for i, slot in enumerate(self.tableau_slots):
            # Add face-down cards to tableau piles with different numbers
            for j in range(i + 1):
                card = Card(tableau_position=(slot.position[0], slot.position[1] - j * tableau_offset))
                slot.cards.append(card)

    def on_draw(self):
        self.clear()

        # Draw the slots
        self.draw_tableau_piles()
        self.draw_foundation_piles()
        self.draw_waste_pile()

    def draw_tableau_piles(self):
        for slot in self.tableau_slots:
            arcade.draw_texture_rectangle(slot.position[0], slot.position[1], 85, 120, self.card_back_texture)

    def draw_foundation_piles(self):
        for slot in self.foundation_slots:
            arcade.draw_rectangle_outline(slot.position[0], slot.position[1], 85, 120,
                                          arcade.color.ASPARAGUS, border_width=5)

    def draw_waste_pile(self):
        arcade.draw_texture_rectangle(self.waste_pile.position[0], self.waste_pile.position[1], 85, 120,
                                      self.card_back_texture)


def main():
    window = Solitaire()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
