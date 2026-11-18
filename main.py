import json
import os
import csv
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

WORDS = {
    "kitob": "O‘qish uchun mo‘ljallangan bosma yoki elektron asar.",
    "ilm": "O‘rganish va izlanish orqali egallanadigan bilim.",
    "vatan": "Inson tug‘ilib o‘sgan yurt.",
    "do‘st": "Yaqin va ishonchli inson.",
    "mehr": "Insonlarga bo‘lgan samimiy iliqlik.",
    "maktab": "Ta’lim beriladigan muassasa.",
    "tabiat": "Bizni o‘rab turgan borliq.",
}

class UzbekLugat(App):
    def build(self):
        self.title = "UZBEK IZOHLI LUG‘AT"

        root = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=10
        )

        title = Label(
            text="📚 UZBEK LUG‘AT",
            font_size=28,
            bold=True,
            color=(0.2, 0.8, 0.5, 1),
            size_hint_y=None,
            height=65
        )
        root.add_widget(title)

        self.search = TextInput(
            hint_text="So‘z kiriting...",
            multiline=False,
            size_hint_y=None,
            height=55
        )
        root.add_widget(self.search)

        btn = Button(
            text="QIDIRISH",
            size_hint_y=None,
            height=55
        )
        btn.bind(on_press=self.search_word)
        root.add_widget(btn)

        self.result = Label(
            text="Lug‘atdan so‘z qidiring!",
            font_size=19,
            halign="left",
            valign="top"
        )
        self.result.bind(
            size=lambda obj, val:
            setattr(obj, "text_size", val)
        )

        scroll = ScrollView()
        scroll.add_widget(self.result)
        root.add_widget(scroll)

        return root

    def search_word(self, instance):
        word = self.search.text.strip().lower()

        if not word:
            self.result.text = "Avval so‘z kiriting!"
            return

        meaning = WORDS.get(word)

        if meaning:
            self.result.text = (
                f"SO‘Z: {word.upper()}\n\n"
                f"IZOH: {meaning}"
            )
        else:
            self.result.text = "Bu so‘z lug‘atda topilmadi."

if __name__ == "__main__":
    UzbekLugat().run()