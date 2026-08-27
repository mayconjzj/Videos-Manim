from manim import *

# Formato vertical 9:16, ideal para Reels do Instagram.
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class EspacosVetoriais(Scene):
    def construct(self):

        # SEÇÃO 1: Título com definição geral de série
        titulo = VGroup(
            Tex(
                r"""
                Espaços Vetoriais \\
                """,
                font_size=36,
            )
        ).arrange(DOWN, buff=0.35)

        self.play(Write(titulo), run_time=2)
        self.wait(8)
        self.play(FadeOut(titulo))

        definicao = VGroup(
            Tex(
                r"""
                 Um espaço vetorial é um conjunto não vazio $V$, munido de uma operação de adição $V \times V \longrightarrow V$ e de uma multiplicação por escalares $K \times V \longrightarrow V$, satisfazendo os axiomas de espaço vetorial.
                """,
                font_size=28,
            )
        ).arrange(DOWN, buff=0.35)

        self.play(Write(definicao), run_time=3)
        self.wait(10)
        self.play(FadeOut(definicao))

        propriedadesTitulo = Tex(
            r"""
            Propriedades de um espaço vetorial:
            """,
            font_size=36,
        )
        definicao2 = Tex(
            r"""
            Seja $V$ um espaço vetorial sobre um corpo $K$. Então, para quaisquer vetores $u, v, w \in V$ e quaisquer escalares $\alpha, \beta \in K$, as seguintes propriedades são satisfeitas:
            """,
            font_size=28,
        )

        propriedade1 = Tex(
            r"""
            1. (Comutatividade da adição) $u + v = v + u$
            """,
            font_size=24,
        )

        propriedade2 = Tex(
            r"""
            2. (Associatividade da adição) $(u + v) + w = u + (v + w)$
            """,
            font_size=24,
        )

        propriedade3 = Tex(
            r"""
            3. (Elemento neutro da adição) Existe um vetor $0 \in V$ \\
            tal que $u + 0 = u$
            """,
            font_size=24,
        )

        propriedade4 = Tex(
            r"""
            4. (Elemento inverso da adição) Para cada vetor $u \in V$, \\
            existe um vetor $-u \in V$ tal que $u + (-u) = 0$
            """,
            font_size=24,
        )

        propriedade5 = Tex(
            r"""
            5. (Distributividade do produto por escalar em relação à \\
            adição de vetores) $\alpha(u + v) = \alpha u + \alpha v$
            """,
            font_size=24,
        )

        propriedade6 = Tex(
            r"""
            6. (Distributividade do produto por escalar em relação à \\
            adição de escalares) \\ $(\alpha + \beta)u = \alpha u + \beta u$
            """,
            font_size=24,
        )

        propriedade7 = Tex(
            r"""
            7. (Associatividade do produto por escalar) $\alpha(\beta u) = (\alpha \beta)u$
            """,
            font_size=24,
        )

        propriedade8 = Tex(
            r"""
            8. (Elemento neutro do produto por escalar) $1u = u$
            """,
            font_size=24,
        )

        propriedadesTitulo.move_to(UP * 2)

        definicao2.next_to(propriedadesTitulo, DOWN, buff=0.35)

        self.play(Write(propriedadesTitulo))
        self.wait(1)

        self.play(Write(definicao2), run_time=4)
        self.wait(5)

        propriedade1.next_to(definicao2, DOWN, 0.35).to_edge(LEFT, buff=1)

        self.play(Write(propriedade1))
        self.wait(5)

        propriedade2.next_to(propriedade1, DOWN, 0.35).align_to(propriedade1, LEFT)

        self.play(Write(propriedade2))
        self.wait(5)

        propriedade3.next_to(propriedade2, DOWN, 0.35).align_to(propriedade1, LEFT)

        self.play(Write(propriedade3))
        self.wait(5)

        propriedade4.next_to(propriedade3, DOWN, 0.35).align_to(propriedade1, LEFT)

        self.play(Write(propriedade4))
        self.wait(5)

        propriedade5.next_to(definicao2, DOWN, buff=0.35).to_edge(RIGHT, buff=1)

        self.play(Write(propriedade5))
        self.wait(5)

        propriedade6.next_to(propriedade5, DOWN, buff=0.35).align_to(propriedade5, LEFT)

        self.play(Write(propriedade6))
        self.wait(6)

        propriedade7.next_to(propriedade6, DOWN, buff=0.35).align_to(propriedade5, LEFT)

        self.play(Write(propriedade7))
        self.wait(5)

        propriedade8.next_to(propriedade7, DOWN, buff=0.35).align_to(propriedade5, LEFT)

        self.play(Write(propriedade8))
        self.wait(5)
