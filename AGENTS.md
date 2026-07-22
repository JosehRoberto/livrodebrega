# Livro do Brega Paraense — Site

> **Este arquivo é lido obrigatoriamente antes de qualquer alteração no projeto.**

---

## 1. Política de Backup — OBRIGATÓRIA

**Todo arquivo modificado DEVE ser copiado para `../backups/livrodebrega/` antes da alteração.**

Convenção:
```
../backups/livrodebrega/<caminho-com-hifens>_YYYYMMDD_HHMMSS.bak
```

Para backup completo do diretório `site/`:
```bash
cp -a site/ ../backups/livrodebrega/site_$(date +%Y%m%d_%H%M%S)
```

## 2. Estrutura do Projeto

```
livrodebrega/
├── site/               # Publicado (Cloudflare Pages)
│   ├── css/style.css
│   ├── img/            # livro-brega-500.png, juniorneves-600.jpg, favicon.png
│   ├── pdf/livro.pdf
│   └── index.html
├── docs/
│   ├── PLANO.md        # Planejamento estratégico (11 fases, incluindo deploy e SEO)
│   ├── plano-de-atualizacao.md  # Plano de migração para gerador JSON+Jinja2
│   └── prompts.md
├── origem/             # Fonte do conteúdo Joomla — não publicado
├── espelho/            # Referência visual Framer — não publicado
├── AGENTS.md
├── CHANGELOG.md
├── README.md
└── .gitignore
```

## 3. Regras de Desenvolvimento

### 3.1 Nomenclatura
- **JSONs:** minúsculas (`livro.json`)
- **Templates:** minúsculas (`index.html`, `base.html`)

### 3.2 Estilo
- CSS customizado puro (sem frameworks)
- Google Fonts via `<link>` (Inter, Antonio, Poppins)
- Cores: azul escuro (`#070D1A`, `#0B1C3A`), azul elétrico (`#0C9AFF`), verde (`#65B01E`)

## 4. Checklist de Alteração

### Antes de editar:
- [x] Backup criado em `../backups/livrodebrega/`
- [x] Classes e IDs do CSS preservados

### Após editar:
- [ ] Verificar renderização no navegador
- [ ] Testar links internos
- [ ] Verificar CSS carregado
- [ ] Atualizar `CHANGELOG.md`

## 5. Content source (`origem/`)

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
