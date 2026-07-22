# As Décadas do Brega Paraense

Landing page do livro **"As Décadas do Brega Paraense — O ritmo, a festa e os cantores"**, de Junior Neves.

Publicado em: [livrodebrega.juniorneves.com](https://livrodebrega.juniorneves.com)

## Sobre

Site estático de página única com informações sobre o e-book, biografia do autor, links para download do PDF, redes sociais e contato.

## Estrutura

```
livrodebrega/
├── site/               # Site publicado (Cloudflare Pages)
│   ├── css/
│   │   └── style.css   # Estilos customizados
│   ├── img/            # Imagens (capa, autor, favicon)
│   ├── pdf/
│   │   └── livro.pdf   # E-book para download
│   └── index.html      # Landing page principal
├── docs/
│   ├── PLANO.md        # Planejamento estratégico
│   └── prompts.md      # Registro de prompts
├── origem/             # Fonte do conteúdo (Joomla export) — não publicado
├── espelho/            # Referência visual Framer — não publicado
├── AGENTS.md           # Instruções para o OpenCode
├── CHANGELOG.md        # Registro de alterações
└── README.md           # Este arquivo
```

## Tecnologias

- HTML5 + CSS3
- Google Fonts (Inter, Antonio, Poppins)
- YouTube embed
- Cloudflare Pages (deploy contínuo via GitHub)

## Deploy

O deploy é automático via Cloudflare Pages ao fazer push na branch `main`:

```bash
git add site/
git commit -m "descrição da mudança"
git push
```

URL de produção: `https://livrodebrega.juniorneves.com`

## Licença

© 2026 Junior Neves. Todos os direitos reservados.
