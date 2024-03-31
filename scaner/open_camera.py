import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture


class CameraApp(App):
    def build(self):
        self.img_texture = Texture.create(size=(640, 480))
        self.camera = cv2.VideoCapture(0)

        layout = BoxLayout(orientation='vertical')

        self.image_widget = Image(texture=self.img_texture)
        layout.add_widget(self.image_widget)

        capture_button = Button(text='Сделать фото')
        capture_button.bind(on_press=self.capture)
        layout.add_widget(capture_button)

        return layout

    def capture(self, event):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.flip(frame, 0)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            self.img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.image_widget.texture = self.img_texture
            self.captured_image = frame
        else:
            print("Ошибка при считывании изображения с камеры")

    def on_stop(self):
        self.camera.release()


if __name__ == '__main__':
    CameraApp().run()