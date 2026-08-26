from manim import *

# Formato vertical 9:16, ideal para Reels do Instagram.
config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920
config.frame_rate = 60


class SeriesMatematicas(Scene):
    def construct(self):

        # SEÇÃO 1: Título com definição geral de série
        titulo = VGroup(
            Tex(
                r"""
            Séries Matemáticas \\
            """,
                font_size=48,
            ).set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED),
            MathTex(r"\sum_{n=1}^{\infty} a_n").set_color_by_gradient(
                BLUE, GREEN, YELLOW, ORANGE, RED
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(titulo), run_time=2)
        self.wait(1)
        self.play(FadeOut(titulo))

        # SEÇÃO 2: Apresentação da sequência (a_n)
        texto1 = VGroup(
            Tex(
                r"""
            Dada uma sequência de números \\
            reais $(a_n)$
            """
            ).set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED),
            MathTex(r"(a_n) = a_1, a_2, a_3, \ldots, a_n").set_color_by_gradient(
                BLUE, GREEN, YELLOW, ORANGE, RED
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto1), run_time=3)
        self.wait(2)
        self.play(FadeOut(texto1))

        # SEÇÃO 3: Introdução às somas parciais S_n
        texto2 = VGroup(
            Tex(
                r"""
            A partir dela formamos uma nova \\
            sequência $(S_n)$ onde
            """
            ).set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED),
            VGroup(
                MathTex(r"S_1 = a_1").set_color_by_gradient(
                    BLUE, GREEN, YELLOW, ORANGE, RED
                ),
                MathTex(r"S_2 = a_1 + a_2").set_color_by_gradient(
                    BLUE, GREEN, YELLOW, ORANGE, RED
                ),
                MathTex(r"\vdots").set_color_by_gradient(
                    BLUE, GREEN, YELLOW, ORANGE, RED
                ),
                MathTex(r"S_n = \sum_{i=1}^n a_i").set_color_by_gradient(
                    BLUE, GREEN, YELLOW, ORANGE, RED
                ),
            ).arrange(DOWN, buff=0.35),
        ).arrange(DOWN, buff=1)

        self.play(Write(texto2), run_time=3)
        self.wait(2)
        self.play(FadeOut(texto2))

        # SEÇÃO 4: Definições finais - somas parciais e termo geral
        texto3 = VGroup(
            Tex(
                r"""
                Os números $S_n$ são chamados de \\
                \textbf{somas parciais} da série $\sum a_n$
                """
            ).set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED),
            Tex(
                r"""
                A parcela $a_n$ é o n-ésimo termo \\
                ou termo geral da série.
                """
            ).set_color_by_gradient(BLUE, GREEN, YELLOW, ORANGE, RED),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto3), run_time=4)
        self.wait(2)
        self.play(FadeOut(texto3))

        self.wait(5)
