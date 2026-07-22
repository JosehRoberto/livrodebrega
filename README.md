# As Décadas do Brega Paraense

Landing page do livro **"As Décadas do Brega Paraense — O ritmo, a festa e os cantores"**, de Junior Neves.

Publicado em: [livrodebrega.juniorneves.com](https://livrodebrega.juniorneves.com)

## Sobre

Site estático de página única com informações sobre o e-book, biografia do autor, links para download do PDF, redes sociais e contato.

## Estrutura

```
livrodebrega/
├── site/               # Site publicado (Cloudflare Pages)
│   ├── css/style.css   # Estilos customizados
│   ├── img/            # Imagens (capa, autor, favicon)
│   ├── pdf/
│   │   └── livro.pdf   # E-book para download
│   └── index.html      # GERADO — não editar manualmente
├── src/                # Código fonte do gerador
│   ├── data/
│   │   └── livro.json  # Conteúdo textual (editar aqui)
│   └── generator/
│       ├── generator.py    # Script de geração (Python + Jinja2)
│       ├── schemas.py      # Validação Pydantic
│       └── templates/      # Jinja2 (base.html, pages/index.html)
├── docs/
│   ├── PLANO.md        # Planejamento estratégico
│   ├── plano-de-atualizacao.md  # Plano de migração
│   └── prompts.md      # Registro de prompts
├── origem/             # Fonte do conteúdo (Joomla export) — não publicado
├── espelho/            # Referência visual Framer — não publicado
├── AGENTS.md           # Instruções para o OpenCode
├── CHANGELOG.md        # Registro de alterações
├── README.md           # Este arquivo
└── requirements.txt    # Dependências Python
```

## Tecnologias

- HTML5 + CSS3
- Google Fonts (Inter, Antonio, Poppins)
- YouTube embed
- Python + Jinja2 (gerador de site estático)
- Pydantic (validação de dados)
- Cloudflare Pages (deploy contínuo via GitHub)

## Desenvolvimento

O conteúdo fica em `src/data/livro.json`. Para regenerar o HTML após editar:

```bash
python3 src/generator/generator.py
```

## Deploy

O deploy é automático via Cloudflare Pages ao fazer push na branch `main`:

```bash
git add src/ site/
git commit -m "descrição da mudança"
git push
```

URL de produção: `https://livrodebrega.juniorneves.com`

## Licença

© 2026 Junior Neves. Todos os direitos reservados.
