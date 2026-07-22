# Changelog — As Décadas do Brega Paraense

> Formato [Keep a Changelog](https://keepachangelog.com/), mais recente primeiro.

## [0.5] — 2026-07-22

### Adicionado
- `src/data/livro.json`: conteúdo textual completo (seo, hero, about, author, social, contact, footer)
- `src/generator/generator.py`: script de geração HTML (Python + Jinja2)
- `src/generator/schemas.py`: validação Pydantic do JSON
- `src/generator/templates/base.html`: layout base com head, header, footer
- `src/generator/templates/pages/index.html`: template da landing page
- `requirements.txt`: dependências (Jinja2, pydantic)

### Alterado
- `site/index.html`: agora é **gerado** pelo generator.py — não editar manualmente
- `AGENTS.md`: estrutura atualizada com `src/`, workflow do gerador, nomenclatura JSON/templates

### Analytics
- **Arquivos novos:** 6 (src/data/livro.json, src/generator/*.py, templates/*.html, requirements.txt)
- **Arquivos alterados:** 2 (AGENTS.md, site/index.html)
- **Gerador:** `python3 src/generator/generator.py` → `site/index.html` (saída validada)
- **Backup:** site/ completo em `../backups/livrodebrega/` antes da migração

## [0.4] — 2026-07-22

### Adicionado
- `docs/plano-de-atualizacao.md`: plano de migração para gerador JSON+Jinja2 (7 fases, riscos, rollback)
- `AGENTS.md`: seção 1 "Política de Backup OBRIGATÓRIA" e seção 4 "Checklist de Alteração"
- `site/index.html`: `<meta name="author">`, `<meta name="theme-color">`, `<link rel="canonical">`, `og:url`, `og:locale`, `og:site_name`, `og:image:width/height/type/alt`, `twitter:image:alt`
- `site/index.html`: JSON-LD structured data (schema.org/Book) com ISBN

### Alterado
- `AGENTS.md`: reestruturado com seções numeradas (backup, estrutura, regras, checklist, conteúdo, referência, workflow)
- `CHANGELOG.md`: reformatado para padrão "Keep a Changelog" com versões, datas e seção Analytics
- `og:image` e `twitter:image`: caminho relativo → URL absoluta (`https://livrodebrega.juniorneves.com/img/...`)

### Analytics
- **Arquivos novos:** 1 (`docs/plano-de-atualizacao.md`)
- **Arquivos alterados:** 3 (AGENTS.md, CHANGELOG.md, site/index.html)
- **Metatags adicionadas:** 12 (6 OG, 1 canonial, 1 author, 1 theme-color, 1 Twitter alt, 1 JSON-LD script)
- **Backup realizado:** `site/` completo em `../backups/livrodebrega/`

---

## [0.3] — 2026-07-22

### Adicionado
- `docs/PLANO.md`: Fase 10 (SEO, Open Graph e Boas Práticas W3C) com diagnóstico e ferramentas de validação

### Alterado
- `site/index.html`: `<head>` reescrito — OG/Twitter tags com absolute URLs, canonical, author, theme-color, locale, site_name, image dimensions
- `site/pdf/livro.pdf` renomeado para `site/pdf/As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf`
- 3 links de download no HTML atualizados para o novo nome do PDF

### Analytics
- **Tags OG:** 9 (type, title, description, url, site_name, locale, image, dimensions, type, alt)
- **Tags Twitter:** 4 (card, title, description, image, image:alt)
- **Structured data:** 1 (JSON-LD Book)
- **SEO checklists:** 16 itens de verificação adicionados

---

## [0.2] — 2026-07-22

### Adicionado
- `README.md`: descrição, estrutura, tecnologias e instruções de deploy
- `site/img/juniorneves-600.jpg`: foto do autor (copiada de `origem/images/livro/`)
- `site/img/favicon.png`: favicon (copiado de `origem/images/livro/`)
- `site/css/`: diretório para estilos
- `site/img/`: diretório para imagens
- `site/pdf/`: diretório para PDF

### Alterado
- `site/style.css` movido para `site/css/style.css`
- `site/livro-brega-500.png` movido para `site/img/livro-brega-500.png`
- Todos os caminhos no HTML atualizados (`css/style.css`, `img/...`, `pdf/...`)
- Remote configurado: `git@github-joseroberto_org:JosehRoberto/livrodebrega.git`
- Repositório iniciado e push realizado
- `docs/PLANO.md`: estrutura de diretórios atualizada, Fase 6 com host SSH `github-joseroberto_org`
- Vídeo MP4 vertical substituído por iframe YouTube horizontal com `aspect-ratio: 16/9`
- Topbar: "Brega Paraense" → "As Décadas do Brega Paraense"
- Capa do livro movida do Hero para a seção Sobre (grid texto + imagem)
- Ícones de redes sociais corrigidos (cada rede com seu SVG correto)
- "ISBN: 978-65-5391-180-2" → "Sobre o E-book" (estilo heading Antonio uppercase)
- `site/PLANO.md` movido para `docs/PLANO.md`

### Analytics
- **Estrutura de diretórios:** 3 pastas criadas (css/, img/, pdf/)
- **Assets copiados:** 3 (juniorneves-600.jpg, favicon.png, livro.pdf)
- **Links de download atualizados:** 3
- **Git:** primeiro push para `JosehRoberto/livrodebrega`
- **Ícones corrigidos:** 5 (Instagram, Facebook, Twitter/X, YouTube, Site)

---

## [0.1] — 2026-07-22

### Adicionado
- `AGENTS.md`: instruções do repositório
- `CHANGELOG.md`: registro de alterações do projeto
- `site/index.html`: landing page completa com Hero, Sobre, Autor, Redes Sociais, Contato, Footer
- `site/css/style.css`: estilos customizados (inspirados em `espelho/b-v2.html`)
- `site/img/livro-brega-500.png`: capa do e-book (copiada de `origem/images/livro/`)
- `site/pdf/As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf`: e-book para download
- `docs/PLANO.md`: planejamento estratégico (9 fases)
- `docs/prompts.md`: registro de prompts do OpenCode

### Analytics
- **Site:** página única responsiva, zero dependências, zero build
- **Seções:** 6 (Topbar, Hero, Sobre, Autor, Redes, Contato, Footer)
- **Assets estáticos:** 4 (1 CSS, 2 imagens, 1 PDF)
- **Google Fonts:** 3 (Inter, Antonio, Poppins)
