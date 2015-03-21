from django.db import models

class MenuItem():
    def __init__(self, Href, Text, CssClass="", Target=""):
        self.Href = Href
        self.Text = Text
        self.CssClass = CssClass
        self.Target = Target



