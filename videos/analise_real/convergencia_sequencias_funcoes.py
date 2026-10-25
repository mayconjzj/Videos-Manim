from manim import *

# Formato horizontal 16:9, seguindo o padrão dos vídeos didáticos do projeto.
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 60


class ConvergenciaFuncoes(Scene):
    def texto_central(self, linhas, font_size=32, cor=WHITE, buff=0.35):
        """Monta um bloco de texto com espaçamento consistente."""
        objetos = VGroup(
            *[
                Tex(linha, font_size=font_size, color=cor)
                for linha in linhas
            ]
        )
        objetos.arrange(DOWN, buff=buff, aligned_edge=ORIGIN)
        return objetos

    def construct(self):
        azul = BLUE_C
        amarelo = YELLOW
        verde = GREEN_C
        vermelho = RED_C

        # 1. Abertura
        titulo = VGroup(
            Tex("Sequências de funções", font_size=48),
            Tex(
                "Convergência pontual e convergência uniforme",
                font_size=30,
                color=azul,
            ),
        ).arrange(DOWN, buff=0.35)

        self.play(Write(titulo), run_time=2.5)
        self.wait(3)
        self.play(FadeOut(titulo))
        self.wait(0.5)

        # 2. O que é uma sequência de funções?
        cabecalho = Tex("Uma sequência de funções", font_size=38, color=azul)
        cabecalho.to_edge(UP, buff=0.5)

        definicao = VGroup(
            Tex("Em vez de uma sequência de números, consideramos funções", font_size=30),
            MathTex(r"f_1, f_2, f_3, \ldots, f_n, \ldots"),
            MathTex(r"f_n : A \longrightarrow \mathbb{R}"),
            Tex("com o mesmo domínio $A$. Fixado $x$, cada $f_n(x)$ é um número.", font_size=27),
        ).arrange(DOWN, buff=0.45)
        definicao.shift(DOWN * 0.25)

        self.play(Write(cabecalho))
        self.play(Write(definicao), run_time=4)
        self.wait(5)
        self.play(FadeOut(cabecalho), FadeOut(definicao))

        # 3. Ideia de convergência pontual
        titulo_pontual = Tex("1. Convergência pontual", font_size=38, color=azul)
        titulo_pontual.to_edge(UP, buff=0.5)

        pontual = VGroup(
            Tex("Escolhemos um ponto $x$ do domínio e observamos os valores", font_size=30),
            MathTex(r"f_1(x),\ f_2(x),\ f_3(x),\ \ldots"),
            Tex("Se esses números convergem para $f(x)$, temos convergência nesse ponto.", font_size=28),
            MathTex(r"\lim_{n\to\infty} f_n(x)=f(x)"),
        ).arrange(DOWN, buff=0.45)
        pontual.shift(DOWN * 0.25)

        self.play(Write(titulo_pontual))
        self.play(Write(pontual), run_time=4)
        self.wait(5)
        self.play(FadeOut(titulo_pontual), FadeOut(pontual))

        # 4. Definição formal da convergência pontual
        formal_pontual = VGroup(
            Tex("Definição", font_size=38, color=azul),
            Tex("A sequência $(f_n)$ converge pontualmente para $f$ em $A$ se", font_size=29),
            MathTex(
                r"\forall x\in A,\quad \lim_{n\to\infty} f_n(x)=f(x)"
            ),
            Tex("Cada ponto pode ter seu próprio ritmo de convergência.", font_size=29, color=amarelo),
        ).arrange(DOWN, buff=0.5)
        self.play(Write(formal_pontual), run_time=4)
        self.wait(5)
        self.play(FadeOut(formal_pontual))

        # 5. Exemplo clássico: f_n(x) = x^n em [0,1]
        exemplo = VGroup(
            Tex("Exemplo: $f_n(x)=x^n$ em $[0,1]$", font_size=36, color=azul),
            MathTex(r"f_1(x)=x,\quad f_2(x)=x^2,\quad f_4(x)=x^4,\quad \ldots"),
        ).arrange(DOWN, buff=0.4)
        exemplo.to_edge(UP, buff=0.45)
        self.play(Write(exemplo), run_time=3)

        axes = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1.2, 0.2],
            x_length=9.5,
            y_length=4.7,
            axis_config={"include_numbers": True, "font_size": 20},
            tips=False,
        ).shift(DOWN * 0.45 + LEFT * 0.25)
        labels = axes.get_axis_labels(
            Tex("$x$", font_size=26),
            Tex("$y$", font_size=26),
        )
        self.play(Create(axes), Write(labels), run_time=2)

        curvas = VGroup()
        for n, cor in [(1, BLUE_C), (2, TEAL), (4, GREEN_C), (8, YELLOW), (16, ORANGE)]:
            curva = axes.plot(
                lambda x, k=n: x**k,
                x_range=[0, 1, 0.01],
                color=cor,
                stroke_width=4,
            )
            curvas.add(curva)
            self.play(Create(curva), run_time=0.9)

        legenda = VGroup(
            *[
                MathTex(rf"n={n}", color=cor, font_size=24)
                for n, cor in [(1, BLUE_C), (2, TEAL), (4, GREEN_C), (8, YELLOW), (16, ORANGE)]
            ]
        ).arrange(RIGHT, buff=0.35).to_edge(DOWN, buff=0.18)
        self.play(FadeIn(legenda))
        self.wait(4)

        observacao = Tex(
            "Quando $n$ cresce, $x^n$ se aproxima de $0$ para todo $x<1$.",
            font_size=25,
            color=amarelo,
        ).to_edge(UP, buff=1.25)
        self.play(Write(observacao))
        self.wait(4)
        self.play(
            FadeOut(exemplo), FadeOut(axes), FadeOut(labels),
            FadeOut(curvas), FadeOut(legenda), FadeOut(observacao)
        )

        # 6. Limite pontual e a exceção no extremo x=1
        titulo_limite = Tex("Qual é a função limite?", font_size=38, color=azul)
        titulo_limite.to_edge(UP, buff=0.5)

        limite = VGroup(
            MathTex(r"\lim_{n\to\infty}x^n=0,\qquad 0\leq x<1"),
            Tex("Mas, no ponto $x=1$:", font_size=30),
            MathTex(r"\lim_{n\to\infty}1^n=1"),
            Tex("Portanto, o limite pontual é a função", font_size=29),
            MathTex(
                r"f(x)=\begin{cases}0,&0\leq x<1,\\1,&x=1.\end{cases}"
            ),
        ).arrange(DOWN, buff=0.45)
        limite.shift(DOWN * 0.2)

        self.play(Write(titulo_limite))
        self.play(Write(limite), run_time=4)
        self.wait(6)
        self.play(FadeOut(titulo_limite), FadeOut(limite))

        # 7. Convergência uniforme: a ideia
        titulo_uniforme = Tex("2. Convergência uniforme", font_size=38, color=azul)
        titulo_uniforme.to_edge(UP, buff=0.5)

        uniforme = VGroup(
            Tex("Agora não basta convergir em cada ponto.", font_size=30),
            Tex("Precisamos controlar o erro em todo o domínio ao mesmo tempo.", font_size=30),
            MathTex(r"|f_n(x)-f(x)|<\varepsilon"),
            Tex("com o mesmo índice $N$ para todos os $x\\in A$.", font_size=29, color=amarelo),
        ).arrange(DOWN, buff=0.5)
        uniforme.shift(DOWN * 0.2)

        self.play(Write(titulo_uniforme))
        self.play(Write(uniforme), run_time=4)
        self.wait(6)
        self.play(FadeOut(titulo_uniforme), FadeOut(uniforme))

        # 8. Definição formal: ordem dos quantificadores
        definicao_uniforme = VGroup(
            Tex("Definição formal", font_size=38, color=azul),
            Tex("A sequência $(f_n)$ converge uniformemente para $f$ em $A$ se", font_size=28),
            MathTex(
                r"\forall\varepsilon>0\ \exists N\in\mathbb{N}\ \forall n\geq N\ \forall x\in A:"
            ),
            MathTex(r"|f_n(x)-f(x)|<\varepsilon"),
            Tex("O mesmo $N$ funciona para todos os pontos do domínio.", font_size=29, color=verde),
        ).arrange(DOWN, buff=0.45)
        self.play(Write(definicao_uniforme), run_time=5)
        self.wait(6)
        self.play(FadeOut(definicao_uniforme))

        # 9. Por que x^n não converge uniformemente em [0,1]?
        titulo_nao_uniforme = Tex("O exemplo $f_n(x)=x^n$ não é uniforme", font_size=36, color=azul)
        titulo_nao_uniforme.to_edge(UP, buff=0.5)

        nao_uniforme = VGroup(
            Tex("Para $x<1$, temos $f(x)=0$; em $x=1$, $f(1)=1$.", font_size=27),
            MathTex(r"\sup_{x\in[0,1]}|f_n(x)-f(x)|=1"),
            Tex("O supremo do erro não diminui com $n$.", font_size=28, color=vermelho),
            Tex("Logo, a convergência é pontual, mas não uniforme.", font_size=30, color=amarelo),
        ).arrange(DOWN, buff=0.5)
        nao_uniforme.shift(DOWN * 0.2)

        self.play(Write(titulo_nao_uniforme))
        self.play(Write(nao_uniforme), run_time=4)
        self.wait(6)
        self.play(FadeOut(titulo_nao_uniforme), FadeOut(nao_uniforme))

        # 10. Exemplo de convergência uniforme
        titulo_exemplo_uniforme = Tex("Um exemplo de convergência uniforme", font_size=36, color=azul)
        titulo_exemplo_uniforme.to_edge(UP, buff=0.5)

        ex_uniforme = VGroup(
            MathTex(r"g_n(x)=\frac{x}{n},\qquad x\in[0,1]"),
            Tex("A função limite é $g(x)=0$.", font_size=29),
            MathTex(r"\sup_{x\in[0,1]}|g_n(x)-g(x)|=\frac{1}{n}"),
            MathTex(r"\frac{1}{n}\longrightarrow 0"),
            Tex("O erro converge a zero uniformemente em $[0,1]$.", font_size=29, color=verde),
        ).arrange(DOWN, buff=0.42)
        ex_uniforme.shift(DOWN * 0.2)

        self.play(Write(titulo_exemplo_uniforme))
        self.play(Write(ex_uniforme), run_time=4)
        self.wait(6)
        self.play(FadeOut(titulo_exemplo_uniforme), FadeOut(ex_uniforme))

        # 11. Comparação direta
        comparacao_titulo = Tex("A diferença essencial", font_size=38, color=azul)
        comparacao_titulo.to_edge(UP, buff=0.5)

        pontual_box = VGroup(
            Tex("Pontual", font_size=34, color=azul),
            Tex("Fixamos $x$ e deixamos $n$ crescer.", font_size=25),
            MathTex(r"\forall x\ \forall\varepsilon\ \exists N_x"),
            Tex("O índice pode depender do ponto.", font_size=24),
        ).arrange(DOWN, buff=0.35)

        uniforme_box = VGroup(
            Tex("Uniforme", font_size=34, color=verde),
            Tex("Controlamos todos os $x$ de uma vez.", font_size=25),
            MathTex(r"\forall\varepsilon\ \exists N\ \forall x"),
            Tex("Um único índice serve para todo o domínio.", font_size=24),
        ).arrange(DOWN, buff=0.35)

        pontual_box.shift(LEFT * 3.7 + DOWN * 0.25)
        uniforme_box.shift(RIGHT * 3.7 + DOWN * 0.25)
        divisor = Line(UP * 1.4, DOWN * 2.2, color=GRAY)

        self.play(Write(comparacao_titulo))
        self.play(Write(pontual_box), Write(uniforme_box), Create(divisor), run_time=4)
        self.wait(7)
        self.play(
            FadeOut(comparacao_titulo), FadeOut(pontual_box),
            FadeOut(uniforme_box), FadeOut(divisor)
        )

        # 12. Fechamento
        fechamento = VGroup(
            Tex("Para lembrar", font_size=40, color=azul),
            Tex("Convergência uniforme implica convergência pontual.", font_size=30),
            MathTex(r"\text{uniforme}\ \Longrightarrow\ \text{pontual}"),
            Tex("A recíproca é falsa: $f_n(x)=x^n$ em $[0,1]$ é o exemplo clássico.", font_size=26),
        ).arrange(DOWN, buff=0.5)

        self.play(Write(fechamento), run_time=4)
        self.wait(8)
        self.play(FadeOut(fechamento))
        self.wait(1)
