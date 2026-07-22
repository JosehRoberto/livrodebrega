# Plano Estratégico — Site "As Décadas do Brega Paraense"

## Objetivo

Construir landing page moderna em `site/index.html` com conteúdo de `origem/` e estilo visual de `espelho/`.

## Escopo

Landing page responsiva de página única (HTML+CSS), sem build system ou framework.

## Conteúdo (origem/index.html)

**Apenas texto e estrutura** — nada é copiado de `origem/` para `site/`.

| Seção | Elementos |
|-------|-----------|
| **Hero** | Título, vídeo vertical (MP4), capa do e-book, botão "Baixar o E-book" |
| **Descrição** | Texto do autor sobre o livro, ISBN |
| **Autor** | Foto (Junior Neves), biografia |
| **Redes Sociais** | Instagram, Facebook, Twitter/X, YouTube, Site |
| **Contato** | WhatsApp, Telefone, Email |
| **Download** | Link para PDF do livro |
| **Footer** | Créditos "Desenvolvido por José Roberto" |

## Assets Visuais (espelho/)

**Imagens, fontes, CSS e ícones** vêm do Framer CDN via `espelho/framerusercontent.com/`. O `site/` referencia os mesmos URLs públicos ou copia os assets locais de `espelho/`.
- Fontes: Google Fonts via `<link>` (Inter, Poppins, Antonio, Archivo, etc.)
- Imagens: `framerusercontent.com/images/...` (capa do livro, autor, favicon, ícones sociais)
- Vídeo: referenciado diretamente de `origem/images/video/livrodebrega_web.mp4`
- PDF: referenciado diretamente de `origem/livro.pdf`

## Estilo Visual (espelho/b-v2.html)

- Design moderno com seções dark/light alternadas
- Tipografia grande e bold
- Cores: azul elétrico (#0c9aff), fundo escuro, texto claro
- Botões CTA com border-radius arredondado
- Fontes: Inter (primária), Antonio, Archivo, Barlow, Montserrat, Open Sans, Poppins, Rubik
- Layout responsivo (Desktop → Mobile)

## Estrutura de Diretórios

```
site/
├── index.html          # Landing page principal (único arquivo)
├── style.css           # Estilos customizados
└── PLANO.md
```

Observação: assets (imagens, vídeo, PDF) são referenciados via URL absoluta a partir do Framer CDN (`framerusercontent.com/`) ou diretamente de `../origem/`. Nenhum asset é copiado para `site/`.

## Etapas de Implementação

### Fase 1 — Preparação
1. ~~Substituir YouTube ID no espelho~~ (concluído)
2. ~~Corrigir `.mjs` de hidratação do Framer~~ (concluído)
3. ~~Criar diretórios em `site/`~~ (concluído)
4. ~~Copiar assets estáticos~~ (desnecessário — assets vêm do Framer CDN)

### Fase 2 — Estrutura HTML
5. Esqueleto HTML5 semântico (`<header>`, `<main>`, `<section>`, `<footer>`)
6. Metatags OG e Twitter Cards
7. Favicon

### Fase 3 — Estilização
8. CSS reset e variáveis (cores, fontes, spacing)
9. Tipografia com Google Fonts (Inter + fallbacks)
10. Grid/flexbox responsivo
11. Seções alternadas (dark/light)
12. Botões CTA com hover
13. Media queries (mobile-first)

### Fase 4 — Conteúdo
14. Seção Hero: título + vídeo + capa + CTA
15. Seção Sobre: texto descritivo + ISBN
16. Seção Autor: foto + biografia
17. Seção Redes: ícones sociais
18. Seção Contato: WhatsApp, telefone, email
19. Footer: copyright + créditos

### Fase 5 — Revisão
20. Validar HTML
21. Testar responsividade
22. Verificar links e assets

### Fase 6 — Versionamento (Git)

23. **Criar `.gitignore`** na raiz do repositório:

    ```gitignore
    # Ignorar assets originais não utilizados
    origem/
    espelho/
    .gitignore

    # Ignorar arquivos do sistema
    .DS_Store
    Thumbs.db
    ```

    > **Observação**: o `site/` é a única pasta que será publicada. `origem/` e `espelho/` são fontes locais que não precisam subir.

24. **Inicializar git** na raiz do projeto (`livrodebrega/`):

    ```bash
    git init
    git add site/ .gitignore
    git commit -m "feat: landing page 'As Décadas do Brega Paraense'"
    ```

25. **Criar repositório no GitHub** (`JosehRoberto/livrodebrega`) — **sem** README, .gitignore ou licença (para evitar conflito no push).

26. **Vincular remote e fazer push:**

    ```bash
    git remote add origin git@github.com:JosehRoberto/livrodebrega.git
    git branch -M main
    git push -u origin main
    ```

### Fase 7 — Cloudflare Pages

27. **Acessar** [Cloudflare Dashboard](https://dash.cloudflare.com/) > **Workers & Pages** > **Create application** > **Pages**.

28. **Conectar ao GitHub**: autorizar Cloudflare Pages a acessar o repositório `JosehRoberto/livrodebrega`.

29. **Configurar o projeto:**

    | Campo | Valor |
    |-------|-------|
    | **Project name** | `livrodebrega` |
    | **Production branch** | `main` |
    | **Build settings** | **Framework preset**: `None` (HTML/JS estático) |
    | **Build command** | _(deixar vazio — sem build)_ |
    | **Build output directory** | `/site` ← **ESSENCIAL**: apontar para dentro do monorepo |
    | **Root directory** | _(deixar vazio)_ |

30. **Aguardar primeiro deploy** — Cloudfare Pages faz o build automático ao detectar o push na `main`.

31. **Verificar URL padrão**: `https://livrodebrega.pages.dev` — testar se o site carrega.

### Fase 8 — Domínio Personalizado

32. **Acessar DNS do domínio** `juniorneves.com` (onde quer que ele esteja hospedado — Cloudflare, Registro.br, etc.).

33. **Adicionar registro CNAME:**

    | Tipo | Nome | Alvo |
    |------|------|------|
    | `CNAME` | `livrodebrega` | `livrodebrega.pages.dev` |

    ⏱ **Propagação DNS**: 1-60 minutos (geralmente <5 min no Cloudflare).

34. **No Cloudflare Pages**, ir em **livrodebrega** > **Custom domains** > **Set up a custom domain**:

    - Digitar `livrodebrega.juniorneves.com`
    - Cloudflare Pages verifica automaticamente o CNAME e emite certificado SSL (Let's Encrypt)

35. **Aguardar certificado SSL** (geralmente <30s).

36. **Testar** `https://livrodebrega.juniorneves.com` — deve redirecionar para o Pages.

### Fase 9 — Deploy Contínuo

37. A cada `git push` na branch `main`, o Cloudflare Pages automaticamente:
    - Detecta mudanças no diretório `site/`
    - Faz deploy incremental
    - Invalida cache do CDN global

38. **Workflow de atualização:**

    ```bash
    # Editar, testar localmente, depois:
    git add site/
    git commit -m "descrição da mudança"
    git push
    ```

### Fase 10 — Checklist de Verificação

- [ ] `https://livrodebrega.pages.dev` carrega corretamente
- [ ] `https://livrodebrega.juniorneves.com` redireciona para o Pages
- [ ] Certificado SSL ativo (cadeado verde)
- [ ] Layout responsivo (mobile/desktop)
- [ ] Vídeo YouTube embed carrega
- [ ] Capa do livro visível na seção Sobre
- [ ] Foto do autor visível
- [ ] PDF do e-book baixa corretamente
- [ ] Links das redes sociais abrem as URLs corretas
- [ ] WhatsApp/telefone/email clicáveis
- [ ] OG tags funcionam (compartilhamento em redes)
- [ ] Favicon aparece na aba do navegador

## Princípios

- **Semântica**: tags HTML5 apropriadas
- **Acessibilidade**: alt text, contraste, labels
- **Performance**: fonts-display swap, lazy loading de vídeo
- **Manutenibilidade**: CSS modular com variáveis
- **Sem dependências**: sem frameworks, sem build steps
