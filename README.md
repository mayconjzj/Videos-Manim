# Videos-Manim

Repositório de vídeos e animações matemáticas produzidos com Python e Manim Community.

## Estrutura

```text
Videos-Manim/
├── videos/
│   ├── analise_real/
│   │   ├── series_matematicas.py
│   │   └── convergencia_sequencias_funcoes.py
│   └── algebra_linear/
│       └── espacos_vetoriais.py
├── .gitignore
├── README.md
└── requirements.txt
```

Cada arquivo contém uma cena independente do Manim, organizada por área matemática.

## Requisitos

- Python 3.10 ou superior, compatível com a versão do Manim instalada.
- Manim Community Edition.
- Uma instalação de LaTeX para renderizar fórmulas com `Tex` e `MathTex`.

Instale as dependências Python:

```bash
python -m pip install -r requirements.txt
```

Consulte a [documentação oficial do Manim](https://docs.manim.community/en/stable/installation.html) para instalar dependências de sistema, incluindo LaTeX e FFmpeg, conforme seu sistema operacional.

## Renderizar uma cena

Na raiz do repositório, execute:

```bash
manim -pqh videos/analise_real/series_matematicas.py SeriesMatematicas
manim -pqh videos/analise_real/convergencia_sequencias_funcoes.py ConvergenciaFuncoes
manim -pqh videos/algebra_linear/espacos_vetoriais.py EspacosVetoriais
```

Use `-pqh` para renderização em qualidade alta com pré-visualização. Para renderizar mais rapidamente durante a edição, troque por `-pql`.

## Organização dos arquivos

- `videos/analise_real/`: cenas sobre sequências, séries e análise real.
- `videos/algebra_linear/`: cenas sobre espaços vetoriais e outros tópicos de álgebra linear.
- Arquivos temporários, caches Python e mídias geradas localmente não devem ser versionados, salvo quando forem resultados finais que se deseja publicar.
