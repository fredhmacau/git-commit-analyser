# gitca — Git Commit Analyser

CLI para analisar o histórico de commits de um repositório Git: quem contribuiu, que áreas do projecto mudaram mais, num período de tempo à escolha.

Projecto de aprendizagem prática, do zero ao deploy, focado em Python, tratamento de erros e estrutura de código.

## Porquê

O histórico de um repositório Git tem informação que raramente é explorada. `gitca` responde a perguntas simples: quem tem contribuído mais nos últimos 90 dias, e que pastas do projecto mudam com mais frequência (o que pode sinalizar zonas instáveis ou áreas que precisam de mais testes).

## Estado actual

- Contagem de commits por autor
- Contagem de commits por área do projecto (directório de topo)
- Filtro por janela de tempo (últimos N dias)
- Tratamento de erros para caminho inválido, repositório inexistente e argumentos em falta
- Resiliente a commits problemáticos (merges, por exemplo) sem abortar a análise inteira

Ainda por fazer: CLI com Click, output formatado com Rich, detecção de qualidade de mensagens (Conventional Commits), comando `suggest` com IA para sugerir mensagens de commit a partir do diff staged, exportação em Markdown/JSON, e publicação no PyPI.

## Instalação (modo desenvolvimento)

```bash
git clone https://github.com/fredhdev/gitca.git
cd gitca
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
```

## Uso

```bash
python main.py /caminho/para/o/repositorio
```

Por omissão analisa os últimos 90 dias e imprime dois dicionários: commits por autor e commits por área do projecto (ex: `{"gitca": 12, "tests": 3}`).

## Estrutura

```
gitca/
├── analyser.py    # leitura do repositório e cálculo de estatísticas
├── main.py        # ponto de entrada da CLI
├── pyproject.toml # packaging (Hatch)
└── README.md
```

## Stack

Python · GitPython · dataclasses · collections.Counter

## Autor

Frederico ([@fredhdev](https://github.com/fredhdev)), Full Stack Developer, 42 Luanda.

## Licença

MIT
READMEEOF
echo "README actualizado."