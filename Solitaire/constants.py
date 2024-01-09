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
