# Livro do Brega Paraense — Site

## Objective

Landing page do livro **"As Décadas do Brega Paraense"** com conteúdo de `origem/` e estilo visual de `espelho/` (Framer). Publicado via Cloudflare Pages em `livrodebrega.juniorneves.com`.

## Estrutura

```
livrodebrega/
├── site/               # Publicado (Cloudflare Pages)
│   ├── css/style.css
│   ├── img/            # livro-brega-500.png, juniorneves-600.jpg, favicon.png
│   ├── pdf/livro.pdf
│   └── index.html
├── docs/
│   ├── PLANO.md        # Planejamento estratégico (10 fases)
│   └── prompts.md
├── origem/             # Fonte do conteúdo Joomla — não publicado
├── espelho/            # Referência visual Framer — não publicado
├── AGENTS.md
├── CHANGELOG.md
├── README.md
└── .gitignore
```

## Content source (`origem/`)

- Title: "As Décadas do Brega Paraense - O ritmo, a festa e os cantores"
- Author: Junior Neves; desktop publishing: José Roberto
- Video: YouTube embed (`WoZWzrQLNWw`) — antes MP4 vertical
- E-book cover: `img/livro-brega-500.png`
- Author photo: `img/juniorneves-600.jpg`
- PDF download: `pdf/livro.pdf`
- Social links: Instagram, Facebook, Twitter/X, YouTube, Website (ícones SVGs corrigidos)
- Contact: WhatsApp +55 91 98345-0690, phone, email
- ISBN: 978-65-5391-180-2
- Language: pt-BR throughout

## Visual reference (`espelho/`)

- Framer-generated responsive single-page layout
- Font families: Antonio, Archivo, Arimo, Barlow, Barlow Condensed, DM Sans, Lexend, Montserrat, Open Sans, Poppins, Rubik
- Modern dark/light sections, large typography, CTA buttons
- Full CSS inline in `b-v2.html`

## Workflow

- Plain HTML/CSS, no build system, no framework
- `site/` é o diretório de publicação (Cloudflare Pages output: `/site`)
- Deploy contínuo via `git push` na `main`
- Remote: `git@github-joseroberto_org:JosehRoberto/livrodebrega.git`
