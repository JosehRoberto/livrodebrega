# Livro do Brega Paraense — Site

## Objective

Build a new site in `site/` using content from `origem/` (Joomla export of "As Décadas do Brega Paraense" landing page) and visual reference from `espelho/` (Framer-generated sales page).

## Layout

| Directory | Purpose |
|-----------|---------|
| `origem/` | Source content (Joomla/Gantry5 HTML + assets). Extract text, images, video, PDF link from here. |
| `espelho/` | Visual reference — Framer landing page. Match layout, typography, spacing, color scheme. |
| `site/` | Target directory for the new site. Start empty. |

## Content source (`origem/index.html`)

- Title: "As Décadas do Brega Paraense - O ritmo, a festa e os cantores"
- Author: Junior Neves; desktop publishing: José Roberto
- Video: `images/video/livrodebrega_web.mp4`
- E-book cover: `images/livro/livro-brega-500.png`
- Author photo: `images/livro/juniorneves-600.jpg`
- PDF download: `livro.pdf`
- Social links: Instagram, Facebook, Twitter/X, YouTube, Website
- Contact: WhatsApp +55 91 98345-0690, phone, email
- ISBN: 978-65-5391-180-2
- Footer: "Desenvolvido por José Roberto" with link to joseroberto.com.br
- Language: pt-BR throughout

## Visual reference (`espelho/`)

- Framer-generated responsive single-page layout
- Font families in use: Antonio, Archivo, Arimo, Barlow, Barlow Condensed, DM Sans, Lexend, Montserrat, Open Sans, Poppins, Rubik
- Modern dark/light sections, large typography, CTA buttons, testimonial-style layout
- Full CSS is inline in `b-v2.html` — extract styles visually, not via @import

## Workflow

- No build system, package manager, or framework detected
- All files are plain HTML/CSS/JS/assets
- Start by creating `site/index.html` from scratch
- Copy needed assets from `origem/` into `site/` (images, video, PDF)
- Reference `espelho/b-v2.html` for layout and styling patterns
- No tests, linter, or formatter configured yet
- No .gitignore — consider adding one before first commit
