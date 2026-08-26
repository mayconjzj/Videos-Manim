from manim import *

# Formato vertical 9:16, ideal para Reels do Instagram.
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60


class SeriesMatematicas(Scene):
    def construct(self):

        titulo = MathTex(r"\text{Series Matemáticas}")

        self.play(Write(titulo))

        self.wait(1)
        self.play(
            FadeOut(titulo),
        )

        serieDefinition = MathTex(r"\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \ldots")

        self.play(Write(serieDefinition))
