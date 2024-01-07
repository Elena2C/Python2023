import arcade


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
