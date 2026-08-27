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
            ),
            MathTex(r"\sum_{n=1}^{\infty} a_n"),
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
            ),
            MathTex(r"(a_n) = a_1, a_2, a_3, \ldots, a_n"),
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
            ),
            VGroup(
                MathTex(r"S_1 = a_1"),
                MathTex(r"S_2 = a_1 + a_2"),
                MathTex(r"\vdots"),
                MathTex(r"S_n = \sum_{i=1}^n a_i"),
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
            ),
            Tex(
                r"""
                A parcela $a_n$ é o n-ésimo termo \\
                ou termo geral da série.
                """
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto3), run_time=4)
        self.wait(2)
        self.play(FadeOut(texto3))

        texto4 = VGroup(
            Tex(
                r"""
                Se exister o limite $\lim_{n \to \infty} S_n$, \\
                diremos que a série $\sum a_n$ é \\
                \textbf{convergente} e \\
                $S = \sum a_n = \sum_{n = 1}^{\infty} a_n = a_1 + a_2 + $\\
                $\ldots + a_n + \ldots$ \\
                será chamado a soma da série. \\
                Se o $\lim_{n \to \infty} S_n$ não existir, \\
                diremos que $\sum a_n$ é uma série \\
                \textbf{divergente}.
                """
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto4), run_time=6)
        self.wait(4)
        self.play(FadeOut(texto4))

        texto5 = VGroup(
            Tex(
                r"""
                Em outras palavras, a série $\sum a_n$ \\
                é convergente se a sequência de \\
                somas parciais $(S_n)$ for convergente.
                """
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto5), run_time=4)
        self.wait(2)
        self.play(FadeOut(texto5))

        texto6 = VGroup(
            Tex(
                r"""
                Exemplo:
                """,
                font_size=48,
            ),
            Tex(
                r"""
                A série $\sum_{n=1}^{\infty} \frac{1}{n^2}$ é convergente, \\
                pois a sequência de somas parciais $(S_n)$ \\
                converge para $\frac{\pi^2}{6}$.
                """
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(texto6), run_time=4)
        self.wait(4)
        self.play(FadeOut(texto6))
