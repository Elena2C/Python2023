import arcade
import random

from card import Card
from constants import *


class Solitaire(arcade.Window):

    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)

        self.card_list = arcade.SpriteList()

        arcade.set_background_color(arcade.color.AMAZON)
        self.held_cards = None
        self.held_cards_original_position = None

        self.foundation_suits = ["hearts", "clubs", "spades", "diamonds"]
        self.foundation_colors = {
            "hearts": arcade.color.RED,
            "clubs": arcade.color.BLUE,
            "spades": arcade.color.YELLOW,
            "diamonds": arcade.color.ORANGE
        }

        # self.pile_mat_list = arcade.SpriteList()
        self.piles = None
        self.game_won = False
        self.show_winning_message = False

        self.win_message_rect_color = arcade.color.LIGHT_GRAY
        self.win_message_text_color = arcade.color.BLACK
        self.win_message_font_size = 20
        self.restart_message = "Press here to restart the game."

        self.setup()

    def setup(self):
        self.held_cards = []
        self.held_cards_original_position = []

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        # stock pile mat
        pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = start_x, bottom_y
        self.pile_mat_list.append(pile)

        # waste pile mat
        pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = start_x + x_spacing, bottom_y
        self.pile_mat_list.append(pile)

        # play piles mats
        for i in range(7):
            pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = start_x + i * x_spacing, middle_y
            self.pile_mat_list.append(pile)

        # foundation pile mats
        for i in range(4):
            pile = arcade.SpriteSolidColor(mat_width, mat_height, arcade.csscolor.DARK_OLIVE_GREEN)
            pile.position = start_x + i * x_spacing, top_y
            self.pile_mat_list.append(pile)

        self.card_list = arcade.SpriteList()

        # Asignarea culorilor fundatiilor
        for pile_index in range(top_pile_1, top_pile_4 + 1):
            mat_color = self.foundation_colors[self.foundation_suits[pile_index - top_pile_1]]
            self.pile_mat_list[pile_index].color = mat_color

        # crearea unui nou set de carti
        for card_suit in card_suits:
            for card_value in card_values:
                card = Card(card_suit, card_value)
                card.position = start_x, bottom_y
                self.card_list.append(card)

        # amestecarea cartilor
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

    def check_for_win(self):
        for pile_index in range(top_pile_1, top_pile_4 + 1):
            if len(self.piles[pile_index]) != 13:
                return False
        return True

    def draw_winning_message(self):
        arcade.draw_rectangle_filled(screen_width // 2, screen_height // 2,
                                     screen_width // 2, screen_height // 4,
                                     self.win_message_rect_color)
        arcade.draw_text("Congratulations! You Won!",
                         screen_width // 2, screen_height // 2 + 20,
                         self.win_message_text_color, font_size=self.win_message_font_size,
                         anchor_x="center", anchor_y="center")
        arcade.draw_text(self.restart_message,
                         screen_width // 2, screen_height // 2 - 20,
                         self.win_message_text_color, font_size=12,
                         anchor_x="center", anchor_y="center")

    @staticmethod
    def get_card_color(suit):
        if suit in ["hearts", "diamonds"]:
            return "red"
        elif suit in ["clubs", "spades"]:
            return "black"

    def pull_to_top(self, card: arcade.Sprite):
        self.card_list.remove(card)
        self.card_list.append(card)

    def validate_foundation_pile(self, card, pile_index):
        # verifica daca tipul cartii se potriveste culorii de pe fundatie
        if card.suit != self.foundation_suits[pile_index - top_pile_1]:
            return False

        if len(self.piles[pile_index]) == 0:
            return card.value == "A"
        else:
            top_card = self.piles[pile_index][-1]
            return card_values.index(card.value) == card_values.index(top_card.value) + 1

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

        if top_pile_1 <= pile_index <= top_pile_4:
            if self.check_for_win():
                self.game_won = True

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup()

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.game_won:
            if screen_width // 2 - screen_width // 4 < x < screen_width // 2 + screen_width // 4 and \
                    screen_height // 2 - screen_height // 8 < y < screen_height // 2 + screen_height // 8:
                self.game_won = False
                self.setup()
            else:
                self.show_winning_message = not self.show_winning_message

        clicked_cards = [card for card in self.card_list if card.collides_with_point((x, y))]

        if clicked_cards:
            primary_card = clicked_cards[-1]
            assert isinstance(primary_card, Card)

            pile_index = self.get_pile_for_card(primary_card)

            if pile_index == bottom_face_down_pile:
                if len(self.piles[bottom_face_down_pile]) > 0:
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
                if len(self.piles[pile_index]) == 0 or (
                        len(self.piles[pile_index]) > 0
                        and card_values.index(self.held_cards[0].value)
                        == card_values.index(self.piles[pile_index][-1].value) - 1
                        #and self.held_cards[0].suit != self.piles[pile_index][-1].suit
                ):
                    top_card = self.piles[pile_index][-1] if len(self.piles[pile_index]) > 0 else None
                    if (top_card is None or
                            (self.held_cards[0].suit != top_card.suit and
                             self.get_card_color(self.held_cards[0].suit) !=
                             self.get_card_color(top_card.suit))):
                        for i, dropped_card in enumerate(self.held_cards):
                            if len(self.piles[pile_index]) > 0:
                                top_card = self.piles[pile_index][-1]
                                dropped_card.position = top_card.center_x, \
                                    top_card.center_y - card_vertical_offset * (i + 1)
                            else:
                                dropped_card.position = pile.center_x, \
                                    pile.center_y - i * card_vertical_offset

                        for card in self.held_cards:
                            self.move_card_to_new_pile(card, pile_index)

                        reset_position = False

            elif top_pile_1 <= pile_index <= top_pile_4 and len(self.held_cards) == 1:
                if self.validate_foundation_pile(self.held_cards[0], pile_index):
                    self.held_cards[0].position = pile.position
                    for i, card in enumerate(self.held_cards):
                        card.position = pile.center_x, \
                            pile.center_y - i * card_vertical_offset
                        self.move_card_to_new_pile(card, pile_index)
                    reset_position = False

        if reset_position:
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        self.held_cards = []

        if self.check_for_win():
            print("Congratulations! You won!")

    def on_draw(self):
        self.clear()

        self.pile_mat_list.draw()
        self.card_list.draw()

        if self.check_for_win():
            self.game_won = True

        if self.game_won:
            self.draw_winning_message()

    def on_close(self):
        self.card_list = None
        #self.pile_mat_list = arcade.SpriteList()
        self.held_cards = None
        self.held_cards_original_position = None

        if self.card_list is not None:
            for card in self.card_list:
                card.texture.dispose()

        if self.pile_mat_list is not None:
            for mat in self.pile_mat_list:
                mat.texture.dispose()
