# Changelog

## [Unreleased]

### Added
- `AGENTS.md` — instruções do repositório
- `site/PLANO.md` — planejamento estratégico para construção da landing page (movido para `docs/PLANO.md` em [2026-07-22])
- `CHANGELOG.md` — registro de alterações do projeto
- `site/index.html` — landing page do zero (HTML + CSS inline)
- `site/style.css` — estilos customizados inspirados em `espelho/b-v2.html` (Framer)
- `site/livro-brega-500.png` — capa do e-book copiada de `origem/`

### Changed
- `espelho/.../b-v2.html` — substituído ID do YouTube `nhF9ccUUQiY` → `WoZWzrQLNWw` no iframe
- `espelho/.../iJlNLBBdtawfDpEpHbe_gVxTHF8MYl3poU4c16B4F2E.gezYvbNZ.mjs` — substituído ID do YouTube `nhF9ccUUQiY` → `WoZWzrQLNWw` nas props do componente (Desktop e Mobile), prevenindo que a hidratação do Framer sobrescrevesse o iframe com o ID antigo
- Vídeo MP4 vertical substituído por iframe YouTube horizontal (`WoZWzrQLNWw`) com `aspect-ratio: 16/9`
- Topbar: título alterado de "Brega Paraense" para "As Décadas do Brega Paraense"
- Capa do livro movida da seção Hero para a seção Sobre, em grid lado a lado com o texto
- Ícones de redes sociais corrigidos (estavam usando SVGs genéricos do `espelho/` — agora cada rede tem seu ícone correto)
- "ISBN: 978-65-5391-180-2" substituído por "Sobre o E-book" com estilo de heading (Antonio uppercase)
- `docs/PLANO.md` — planejamento movido de `site/` para `docs/`
