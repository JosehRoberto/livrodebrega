# Plano de Atualização — Gerador de Site Estático (JSON + Jinja2)

## 1. Objetivo

Migrar a landing page de `site/index.html` (HTML puro) para um gerador de site estático Python + Jinja2, reutilizando a arquitetura já consolidada do projeto `juniorneves-bot`. O conteúdo textual sai do HTML e vai para arquivos JSON; o HTML é gerado por templates Jinja2.

A alteração **não pode quebrar o site atual** — o deploy contínuo via Cloudflare Pages deve continuar funcionando ininterruptamente.

## 2. Estrutura-Alvo

```
site/                           # Publicado (Cloudflare Pages)
├── css/style.css               # Inalterado
├── img/                        # Inalterado
├── pdf/                        # Inalterado
├── index.html                  # AGORA GERADO pelo generator.py
└── .opencode/                  # Skill OpenCode (similar ao juniorneves-site)
    └── skills/
        └── livro-brega/
            └── SKILL.md

src/                            # NOVO — código fonte do gerador
├── data/
│   └── livro.json              # Conteúdo textual extraído do index.html atual
├── generator/
│   ├── generator.py            # Script de geração (Python + Jinja2)
│   ├── schemas.py              # Validação Pydantic dos dados
│   └── templates/
│       ├── base.html           # Layout base (DOCTYPE, head, topbar, footer)
│       └── pages/
│           └── index.html      # Template específico da landing page

docs/                           # Inalterado
origem/                         # Inalterado
espelho/                        # Inalterado
```

## 3. Estratégia de Backup — OBRIGATÓRIA

Antes de qualquer alteração nos arquivos de `site/`, fazer backup completo:

```bash
cp -a /home/roberto/projetos/livrodebrega/site /home/roberto/projetos/backups/livrodebrega/site_$(date +%Y%m%d_%H%M%S)
```

Para arquivos individuais:
```
../backups/livrodebrega/<caminho-com-hifens>_YYYYMMDD_HHMMSS.bak
```

### Plano de Rollback

Se o site gerado apresentar qualquer problema após o deploy:

```bash
# 1. Restaurar backup completo
rm -rf site/
cp -a /home/roberto/projetos/backups/livrodebrega/site_<TIMESTAMP>/ site/

# 2. Se o backup tiver sido sobrescrito, usar git:
git checkout main -- site/
```

## 4. Etapas de Execução

### Fase 1 — Preparação e Backup

- [ ] Criar diretório `src/` com subdiretórios `data/`, `generator/`, `generator/templates/`, `generator/templates/pages/`
- [ ] Fazer backup completo de `site/` para `../backups/livrodebrega/`
- [ ] Verificar que o site atual está íntegro (abrir `site/index.html` no navegador)

### Fase 2 — Extrair dados para JSON

- [ ] Criar `src/data/livro.json` com todo o conteúdo textual do site:
  - Dados do e-book (título, autor, ISBN, descrição)
  - Biografia do autor
  - Redes sociais (Instagram, Facebook, Twitter/X, YouTube, Site)
  - Contato (WhatsApp, telefone, email)
  - Configurações de SEO (title, meta description, OG tags)
- [ ] Validar JSON com Pydantic (`schemas.py`)

### Fase 3 — Criar templates Jinja2

- [ ] Criar `src/generator/templates/base.html`:
  - DOCTYPE + `<html lang="pt-BR">`
  - `<head>` com todas as meta tags (OG, Twitter, JSON-LD, canonical, theme-color)
  - Google Fonts
  - Topbar (dados de `livro.json`)
  - Footer (dados de `livro.json`)
  - `{% block content %}` para o conteúdo da página
- [ ] Criar `src/generator/templates/pages/index.html`:
  - Seção Hero (título, vídeo YouTube, CTA)
  - Seção Sobre (texto + capa do livro em grid)
  - Seção Autor (foto + biografia)
  - Seção Redes Sociais (ícones SVGs)
  - Seção Contato (WhatsApp, telefone, email)

### Fase 4 — Escrever generator.py

- [ ] Adaptar `generator.py` do `juniorneves-bot` (simplificar para página única):
  ```python
  import json
  from pathlib import Path
  from jinja2 import Environment, FileSystemLoader

  # Caminhos
  BASE_DIR = Path(__file__).resolve().parent.parent.parent
  SITE_DIR = BASE_DIR / "site"
  DATA_DIR = BASE_DIR / "src" / "data"
  TEMPLATES_DIR = BASE_DIR / "src" / "generator" / "templates"

  # Carregar dados
  with open(DATA_DIR / "livro.json") as f:
      livro = json.load(f)

  # Jinja2
  env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

  # Renderizar página única
  template = env.get_template("pages/index.html")
  output = template.render(livro=livro, root_path=".")

  with open(SITE_DIR / "index.html", "w") as f:
      f.write(output)
  ```
- [ ] Testar: `python3 src/generator/generator.py` deve produzir HTML idêntico ao atual

### Fase 5 — Validação

- [ ] `diff -u site/index.html backup_site/index.html` — zero diferenças (exceto formatação)
- [ ] Abrir no navegador: layout, fontes, cores, links idênticos
- [ ] Testar responsividade (mobile/desktop)
- [ ] Verificar OG tags no Facebook Sharing Debugger
- [ ] Verificar Twitter Card no validador

### Fase 6 — Deploy

- [ ] Adicionar dependências ao `requirements.txt`: `Jinja2>=3.1`, `pydantic>=2.0`
- [ ] Atualizar `.gitignore` se necessário
- [ ] `git add . && git commit -m "feat: gerador de site estático JSON+Jinja2"`
- [ ] `git push` → Cloudflare Pages auto-deploy
- [ ] Verificar `https://livrodebrega.juniorneves.com` no ar

### Fase 7 — Skill OpenCode (opcional)

- [ ] Criar `.opencode/skills/livro-brega/SKILL.md` com comandos:
  - `deploy` — generator.py + git add/commit/push
  - `edit <campo>` — backup → editar JSON → regenerar
  - `audit` — verificar consistência entre JSON e HTML gerado

## 5. Adaptações do juniorneves-bot

| No juniorneves-bot | No livrodebrega |
|---|---|
| 12 JSONs (artista, menu, home, blog, ...) | 1 JSON (`livro.json`) |
| 9 templates de página | 1 template (`pages/index.html`) |
| 14 partials | 0 partials (opcional se quiser separar) |
| Gantry 5 / JL UIkit classes | CSS customizado puro |
| URLs clean (diretórios) | Página única (`index.html` na raiz) |
| Deploy FTP + Cloudflare Pages | Apenas Cloudflare Pages |

## 6. Riscos e Mitigação

| Risco | Probabilidade | Mitigação |
|-------|:---:|---|
| HTML gerado diferente do atual | Média | `diff` antes do deploy; backup disponível |
| JSON-LD/OG tags quebradas | Baixa | Testar no Sharing Debugger |
| CSS quebrado | Baixa | CSS permanece inalterado em `site/css/style.css` |
| Pipeline de deploy falha | Baixa | Deploy manual via `git push` — já testado |
| Perda de edições manuais | Baixa | Backup completo antes de qualquer alteração |

## 7. Autorização

**Este plano só deve ser executado após aprovação explícita do mantenedor do projeto.**

---

*Plano criado em 2026-07-22 — baseado na arquitetura do juniorneves-bot v1.80*
