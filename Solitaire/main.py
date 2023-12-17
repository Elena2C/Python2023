import random
import arcade

screen_width = 1024
screen_height = 768
screen_title = "Game_Interface"
tableau_offset = 20

card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_suits = ["hearts", "clubs", "spades", "diamonds"]

card_scale = 0.6
card_width = 140 * card_scale
card_height = 190 * card_scale

mat_percent_oversize = 1.25
mat_height = int(card_height * mat_percent_oversize)
mat_width = int(card_width * mat_percent_oversize)

vertical_margin_percent = 0.10
horizontal_margin_percent = 0.10

bottom_y = mat_height / 2 + mat_height * vertical_margin_percent
start_x = mat_width / 2 + mat_width * horizontal_margin_percent

top_y = screen_height - mat_height / 2 - mat_height * vertical_margin_percent

middle_y = top_y - mat_height - mat_height * vertical_margin_percent

x_spacing = mat_width + mat_width * horizontal_margin_percent

card_vertical_offset = card_height * card_scale * 0.3

pile_count = 13
bottom_face_down_pile = 0
bottom_face_up_pile = 1
play_pile_1 = 2
play_pile_2 = 3
play_pile_3 = 4
play_pile_4 = 5
play_pile_5 = 6
play_pile_6 = 7
play_pile_7 = 8
top_pile_1 = 9
top_pile_2 = 10
top_pile_3 = 11
top_pile_4 = 12


class Card(arcade.Sprite):
    def __init__(self, suit, value, scale=0.65):

        self.suit = suit
        self.value = value

        self.image_file_name = f"cards/{self.suit}{self.value}.png"
        self.face_down_image = "cards/CardBack.png"
        self.is_face_up = False

        super().__init__(self.face_down_image, scale, hit_box_algorithm="None")

        self.width *= scale
        self.height *= scale

    def face_down(self, scale=0.65):
        self.texture = arcade.load_texture(self.face_down_image)
        self.is_face_up = False
        self.width *= scale
        self.height *= scale

    def face_up(self, scale=0.65):
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True
        self.width *= scale
        self.height *= scale

    @property
    def is_face_down(self):
        return not self.is_face_up


class Solitaire(arcade.Window):

    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)

        self.card_list = None

        arcade.set_background_color(arcade.color.AMAZON)
        self.held_cards = None
        self.held_cards_original_position = None

        self.pile_mat_list = None
        self.piles = None

    def setup(self):
        self.held_cards = []
        self.held_cards_original_position = []

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = start_x, bottom_y
        self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = start_x + x_spacing, bottom_y
        self.pile_mat_list.append(pile)

        for i in range(7):
            pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = start_x + i * x_spacing, middle_y
            self.pile_mat_list.append(pile)

        for i in range(4):
            pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = start_x + i * x_spacing, top_y
            self.pile_mat_list.append(pile)

        self.card_list = arcade.SpriteList()

        for card_suit in card_suits:
            for card_value in card_values:
                card = Card(card_suit, card_value)
                card.position = start_x, bottom_y
                self.card_list.append(card)

        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        self.piles = [[] for _ in range(pile_count)]
        for card in self.card_list:
            self.piles[bottom_face_down_pile].append(card)

        for pile_no in range(play_pile_1, play_pile_7 + 1):
            for j in range(pile_no - play_pile_1 + 1):
                card = self.piles[bottom_face_down_pile].pop()
                self.piles[pile_no].append(card)
                card.position = self.pile_mat_list[pile_no].position
                self.pull_to_top(card)

        for i in range(play_pile_1, play_pile_7 + 1):
            self.piles[i][-1].face_up()

    def pull_to_top(self, card: arcade.Sprite):
        self.card_list.remove(card)
        self.card_list.append(card)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup()

    def on_mouse_press(self, x, y, button, key_modifiers):
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        if len(cards) > 0:
            primary_card = cards[-1]
            assert isinstance(primary_card, Card)
            pile_index = self.get_pile_for_card(primary_card)
            if pile_index == bottom_face_down_pile:
                for i in range(3):
                    if len(self.piles[bottom_face_down_pile]) == 0:
                        break
                    card = self.piles[bottom_face_down_pile][-1]
                    card.face_up()
                    card.position = self.pile_mat_list[bottom_face_up_pile].position
                    self.piles[bottom_face_down_pile].remove(card)
                    self.piles[bottom_face_up_pile].append(card)
                    self.pull_to_top(card)

            elif primary_card.is_face_down:
                primary_card.face_up()
            else:
                self.held_cards = [primary_card]
                self.held_cards_original_position = [self.held_cards[0].position]
                self.pull_to_top(self.held_cards[0])

                card_index = self.piles[pile_index].index(primary_card)
                for i in range(card_index + 1, len(self.piles[pile_index])):
                    card = self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_original_position.append(card.position)
                    self.pull_to_top(card)

        else:
            mats = arcade.get_sprites_at_point((x, y), self.pile_mat_list)
            if len(mats) > 0:
                mat = mats[0]
                mat_index = self.pile_mat_list.index(mat)
                if mat_index == bottom_face_down_pile and len(self.piles[bottom_face_down_pile]) == 0:
                    temp_list = self.piles[bottom_face_up_pile].copy()
                    for card in reversed(temp_list):
                        card.face_down()
                        self.piles[bottom_face_up_pile].remove(card)
                        self.piles[bottom_face_down_pile].append(card)
                        card.position = self.pile_mat_list[bottom_face_down_pile].position

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if len(self.held_cards) == 0:
            return

        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        if arcade.check_for_collision(self.held_cards[0], pile):
            pile_index = self.pile_mat_list.index(pile)
            if pile_index == self.get_pile_for_card(self.held_cards[0]):
                pass

            elif play_pile_1 <= pile_index <= play_pile_7:
                if len(self.piles[pile_index]) > 0:
                    top_card = self.piles[pile_index][-1]
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                            top_card.center_y - card_vertical_offset * (i + 1)
                else:
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - card_vertical_offset * i

                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

            elif top_pile_1 <= pile_index <= top_pile_4 and len(self.held_cards) == 1:
                self.held_cards[0].position = pile.position
                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

        if reset_position:
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        self.held_cards = []

    def get_pile_for_card(self, card):
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def remove_card_from_pile(self, card):
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def move_card_to_new_pile(self, card, pile_index):
        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

    def on_draw(self):
        self.clear()

        self.pile_mat_list.draw()

        self.card_list.draw()


def main():
    window = Solitaire()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
