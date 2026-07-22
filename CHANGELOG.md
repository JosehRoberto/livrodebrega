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
- `docs/PLANO.md` — planejamento estratégico (10 fases, incluindo deploy)
- `docs/prompts.md` — registro de prompts

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
