import arcade
import random
import sys

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
        '''
        Initializeaza cartea cu valoarea si tipul.
        Suit: Indica tipul cartii (inima, romb, trefla sau pica)
        value: Indica valoarea unei carti (A, 2, ..., 10, J, Q, K)
        scale: Parametru folosit pentru formatarea egala a cartilor
        '''

        self.suit = suit
        self.value = value

        self.image_file_name = f"../cards/{self.suit}{self.value}.png"
        self.face_down_image = "../cards/CardBack.png"
        self.is_face_up = False

        super().__init__(self.face_down_image, scale, hit_box_algorithm="None")

        self.width *= scale
        self.height *= scale

    def face_down(self, scale=0.65):
        '''

        Aseaza cartile cu fata in jos
        '''

        self.texture = arcade.load_texture(self.face_down_image)
        self.is_face_up = False
        self.width *= scale
        self.height *= scale

    def face_up(self, scale=0.65):
        '''
        Intoarce cartea cu fata in sus

        '''
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True
        self.width *= scale
        self.height *= scale

    @property
    def is_face_down(self):
        '''
        Proprietate pentru a verifica daca o carte este cu fata in jos
        '''
        return not self.is_face_up


class Solitaire(arcade.Window):

    def __init__(self):
        '''
        Inițializează fereastra de joc, creând o instanță a clasei Solitaire
        care servește drept fereastra principală a jocului. Această metodă
        configurează starea inițială a jocului, inclusiv dimensiunile ferestrei
        de joc, titlul, culoarea de fundal și inițializează diverse atribute
        precum liste de cărți, fundatiile și sloturile pentru gramezile de joc. În plus,
        pregătește mediul de joc prin crearea de grămezi de cărți, amestecarea
        acestora și asigurarea că fundatiile au culorile inițiale
        atribuite.
        '''
        super().__init__(screen_width, screen_height, screen_title)

        # liste pentru stocarea cartilor
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

        self.pile_mat_list = arcade.SpriteList()
        self.piles = None
        self.game_won = False
        self.show_winning_message = False

        self.win_message_rect_color = arcade.color.LIGHT_GRAY
        self.win_message_text_color = arcade.color.BLACK
        self.win_message_font_size = 20
        self.restart_message = "Press here to restart the game."

        self.setup()

    def setup(self):
        '''
        Configurează starea inițială a jocului, punând în ordine mediul de joc
        Solitaire prin crearea și aranjarea diverselor elemente. Acest lucru
        include definirea tipului și culorilor
        fundatiilor, inițializarea listelor de cărți și generarea grămezilor
        de cărți. Metoda coordonează poziționarea acestor elemente, asigurând
        un punct de plecare pentru joc. De asemenea,
        administrează randomizarea pozițiilor cărților și, în cazul fundatiilor,
        atribuie culori specifice în funcție tipul lor
        corespunzător (rosu pentru inima, albastru pentru trefla, verde pentru pica,
        oranj pentru romb).
        '''

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

        self.piles = [[] for _ in range(pile_count)]

        # Assign colors to foundation piles
        for pile_index in range(top_pile_1, top_pile_4 + 1):
            mat_color = self.foundation_colors[self.foundation_suits[pile_index - top_pile_1]]
            self.pile_mat_list[pile_index].color = mat_color

        for card in self.card_list:
            self.piles[bottom_face_down_pile].append(card)

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

    def check_for_win(self):
        '''
        Verifică dacă jocul a fost câștigat prin examinarea fundatiilor.
        Funcția analizează fiecare grămadă pentru a verifica daca are toate cele 13 cărți,
        semnalând astfel victoria în jocul Solitaire. Returnează o valoare booleană.
        '''

        for pile_index in range(top_pile_1, top_pile_4 + 1):
            if len(self.piles[pile_index]) != 13:
                return False
        return True

    def draw_winning_message(self):
        '''
        Afișează un mesaj de victorie când jucătorul finalizează cu succes Solitaire.
        '''

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
        '''
        Returneaza culoarea in fucntie de tipul cartii.
        '''
        if suit in ["hearts", "diamonds"]:
            return "red"
        elif suit in ["clubs", "spades"]:
            return "black"

    def pull_to_top(self, card: arcade.Sprite):
        '''
        Plasează o carte la vârful listei pentru desenare, asigurând vizibilitate maximă.
        Elimină cartea din poziția sa curentă și o adaugă la sfârșit, menținând
        ierarhia vizuală corectă. Susține vizualizarea fluentă a mișcărilor și
        interacțiunilor cu cărțile în joc.
        '''

        self.card_list.remove(card)
        self.card_list.append(card)

    def validate_foundation_pile(self, card, pile_index):
        '''
        Validează mutarea unei cărți pe o fundatie,
        ținând cont de regulile jocului Solitaire.
        '''

        # Check if the card suits match the foundation pile's suit
        if card.suit != self.foundation_suits[pile_index - top_pile_1]:
            return False

            # Check if the foundation pile is empty and the card is an Ace
        if len(self.piles[pile_index]) == 0:
            return card.value == "A"
        else:
            # Check if the card value is the next in sequence
            top_card = self.piles[pile_index][-1]
            return card_values.index(card.value) == card_values.index(top_card.value) + 1

    def get_pile_for_card(self, card):
        '''
        Returnează indexul teancului care conține o carte specifică.
        '''
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def remove_card_from_pile(self, card):
        '''
        Elimină o carte din teancul său curent.
        '''
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def move_card_to_new_pile(self, card, pile_index):
        '''
        Mută o carte la un teanc nou, ajustându-i poziția și verificând câștigul prin
        examinarea fundatiilor.
        '''

        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

        if top_pile_1 <= pile_index <= top_pile_4:
            if self.check_for_win():
                self.game_won = True

    def restart(self, symbol: int):
        '''
        Restarteaza jocul
        '''

        if symbol == arcade.key.R:
            self.setup()

    def on_mouse_press(self, x, y, button, key_modifiers):
        '''
        Această funcție reacționează la interacțiunile cu mouse-ul, identificând
        cărțile apăsate, verificând orientarea lor și executând acțiuni corespunzătoare.
        De asemenea, gestionează acțiunile legate de starea de câștig a jocului, permitând
        tranziții fără probleme între sesiunile de joc.
        '''

        if self.game_won:
            if screen_width // 2 - screen_width // 4 < x < screen_width // 2 + screen_width // 4 and \
                    screen_height // 2 - screen_height // 8 < y < screen_height // 2 + screen_height // 8:
                self.game_won = False
                self.setup()
            else:
                self.show_winning_message = not self.show_winning_message

        # Check if the mouse click is on any card
        clicked_cards = [card for card in self.card_list if card.collides_with_point((x, y))]

        if clicked_cards:
            primary_card = clicked_cards[-1]  # Take the topmost card if multiple cards are clicked
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
        '''
        Gestionează evenimentele de mișcare a mouse-ului în timpul jocului.
        Această funcție răspunde activ la mișcarea mouse-ului de către utilizator,
        în special în timpul tragerii cărților.
        '''

        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        '''
        Gestionează evenimentele de eliberare a mouse-ului, care au loc atunci când jucătorul
        eliberează butonul mouse-ului după interacțiunea cu interfața jocului.
        Prin răspunsul la evenimentele de eliberare a mouse-ului, logica jocului poate evalua dacă
        mutarea este validă, facilitând plasarea cărților sau declanșarea resetărilor necesare.
        '''

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
                        and self.held_cards[0].suit != self.piles[pile_index][-1].suit
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
        '''
        Desenează fereastra jocului.
        '''
        self.clear()

        self.pile_mat_list.draw()
        self.card_list.draw()

        if self.check_for_win():
            self.game_won = True

        if self.game_won:
            self.draw_winning_message()

    def on_close(self):
        '''
        Eliberează resursele jocului Solitaire la închiderea ferestrei,
        prevenind scurgerile de memorie și asigurând o experiență de utilizare stabilă.
        '''

        # Release resources when the window is closed
        self.card_list = None
        self.pile_mat_list = arcade.SpriteList()
        self.held_cards = None
        self.held_cards_original_position = None

        # Dispose textures in card_list
        if self.card_list is not None:
            for card in self.card_list:
                card.texture.dispose()

        # Dispose textures in pile_mat_list
        if self.pile_mat_list is not None:
            for mat in self.pile_mat_list:
                mat.texture.dispose()


def main():
    '''
    Funcția principală pentru crearea ferestrei Solitaire și rularea jocului.
    '''
    #window = Solitaire()
    #window.setup()
    #arcade.run()


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    with open('game_module.py', 'w', encoding='utf-8') as f:
        f.write('''\
"""
Game module
===============

This module provides a function to initialize a game of Solitaire

"""

''' + open(sys.argv[0], encoding='utf-8').read())

        import pydoc
        pydoc.writedoc('game_module')
