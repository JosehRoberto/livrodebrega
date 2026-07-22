# Changelog

## [Unreleased]

### Added
- `AGENTS.md` — instruções do repositório
- `CHANGELOG.md` — registro de alterações do projeto
- `README.md` — descrição, estrutura, tecnologias e instruções de deploy
- `site/index.html` — landing page do zero
- `site/css/style.css` — estilos customizados inspirados em `espelho/b-v2.html`
- `site/img/livro-brega-500.png` — capa do e-book
- `site/img/juniorneves-600.jpg` — foto do autor (copiada de `origem/`)
- `site/img/favicon.png` — favicon (copiado de `origem/`)
- `site/pdf/livro.pdf` — e-book para download (copiado de `origem/`)
- `docs/PLANO.md` — planejamento estratégico (11 fases, incluindo deploy e SEO)
- `docs/prompts.md` — registro de prompts
- `site/index.html` — JSON-LD structured data (schema.org/Book) com ISBN
- `site/index.html` — metatags: `author`, `theme-color`, `canonical`, `og:url`, `og:locale`, `og:site_name`, `og:image:width/height/type/alt`, `twitter:image:alt`

### Changed
- `espelho/.../b-v2.html` — YouTube ID `nhF9ccUUQiY` → `WoZWzrQLNWw`
- `espelho/.../*.mjs` — YouTube ID atualizado nas props (Desktop e Mobile)
- Vídeo MP4 vertical substituído por iframe YouTube horizontal (`aspect-ratio: 16/9`)
- Topbar: título alterado de "Brega Paraense" para "As Décadas do Brega Paraense"
- Capa do livro movida da seção Hero para a seção Sobre (grid texto + imagem)
- Ícones de redes sociais corrigidos (SVGs corretos por rede)
- "ISBN: 978-65-5391-180-2" → "Sobre o E-book" (estilo heading)
- Estrutura organizada: `css/`, `img/`, `pdf/` em `site/`
- `site/PLANO.md` movido para `docs/PLANO.md`
- Remote configurado: `git@github-joseroberto_org:JosehRoberto/livrodebrega.git`
- Repositório iniciado e push realizado para `JosehRoberto/livrodebrega`
- `og:image` e `twitter:image` — caminho relativo → URL absoluta (`https://livrodebrega.juniorneves.com/img/...`)
- `docs/PLANO.md` — adicionada Fase 10 (SEO, OG e W3C) com diagnóstico e ferramentas de validação
