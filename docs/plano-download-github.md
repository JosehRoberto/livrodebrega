# Plano de Download com Notificação - GitHub Releases + GitHub Actions

## Objetivo

Implementar sistema de download do PDF do e-book com notificação automática por e-mail para `contato@juniorneves.com`, utilizando os recursos nativos do GitHub (Releases + Actions).

## Visão Geral

```
Usuário → site/index.html → Link GitHub Releases → Download PDF → GitHub Action → Email Notificação
```

## Estrutura Atual

```
livrodebrega/
├── site/
│   └── index.html          # Precisa atualizar link de download
├── src/
│   ├── data/livro.json     # Contém: pdf_download
│   └── generator/          # Gerador Jinja2
├── docs/
│   └── plano-download-github.md  # ESTE ARQUIVO
└── .github/
    └── workflows/          # NOVO: Actions para notificação
```

## Recursos do GitHub (Grátis)

| Recurso | Limite | Status |
|---------|--------|--------|
| **Actions** | 2.000 minutos/mês | ✅ Suficiente |
| **Releases** | 1.000 | ✅ Suficiente |
| **Download/Release** | Ilimitado | ✅ Ideal |
| **Armazenamento** | 2 GB/repo | ✅ PDF = 18 MB |
| **CDN** | GitHub Pages CDN | ✅ Global |

## Etapas de Implementação

### Fase 1: Preparação

- [ ] Verificar espaço em `src/data/livro.json` para novo campo `pdf_url`
- [ ] Atualizar template `src/generator/templates/pages/index.html` para usar novo link
- [ ] Criar diretório `.github/workflows/`

### Fase 2: Upload do PDF

**Opção A: Manual via GitHub Web UI**
1. Acessar https://github.com/JosehRoberto/livrodebrega/releases
2. Criar novo release (ex: `v1.0`)
3. Upload do PDF: `As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf`
4. Publicar release

**Opção B: Via CLI**
```bash
gh release create v1.0 ./site/pdf/As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf \
  --title "E-book - As Décadas do Brega Paraense" \
  --notes "Download do e-book completo"
```

### Fase 3: Configuração de Notificação (Zoho Mail)

**Arquivo: `.github/workflows/download-notification.yml`**

```yaml
name: Download Notification
on:
  release:
    types: [published]
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send download notification
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: smtp.zoho.com
          server_port: 465
          username: ${{ secrets.ZOHO_SMTP_USER }}
          password: ${{ secrets.ZOHO_SMTP_PASSWORD }}
          subject: "Novo download do e-book 'As Décadas do Brega Paraense'"
          body: |
            Um novo download foi realizado!
            
            Link: ${{ github.event.release.html_url }}
            Tag: ${{ github.event.release.tag_name }}
            Data: $(date)
          to: contato@juniorneves.com
          from: contato@juniorneves.com
          ssl: true
```

### Fase 4: Atualização do Site

**Arquivo: `src/data/livro.json`**
```json
{
  "pdf_url": "https://github.com/JosehRoberto/livrodebrega/releases/latest/download/As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf",
  "pdf_download": "pdf/As-Decadas-do-Brega-Paraense-O-Ritmo-A-Festa-e-os-Cantores-Junior-Neves.pdf"
}
```

**Arquivo: `src/generator/templates/pages/index.html`**
```html
<a href="{{ livro.pdf_url }}" class="btn btn-primary" download>
  Baixar o E-book
</a>
```

### Fase 5: Deploy

```bash
# 1. Commitar mudanças
git add .github/ src/
git commit -m "feat: download via GitHub Releases + notification"

# 2. Push
git push origin main

# 3. Cloudflare Pages redeploy automático
```

## Alternativas de Notificação

### Alternativa 1: Zapier (Grátis - 100 tarefas/mês)
```
GitHub Webhook → Zapier → Gmail
```

### Alternativa 2: Make (Grátis - 1.000 operações/mês)
```
GitHub Trigger → Make Scenario → Email
```

### Alternativa 3: Webhook Custom
```yaml
# .github/workflows/webhook-notify.yml
- name: Trigger webhook
  run: |
    curl -X POST https://hooks.zapier.com/hooks/catch/123456/abcdef/ \
      -H "Content-Type: application/json" \
      -d '{"event":"download","url":"${{ github.event.release.html_url }}"}'
```

## Fluxo de Trabalho

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Usuário clica em "Baixar E-book"                        │
│                                                             │
│ 2. Redireciona para GitHub Releases                        │
│     ↓                                                        │
│ 3. Usuário clica em "Download"                               │
│     ↓                                                        │
│ 4. GitHub dispara evento "release.published"                 │
│     ↓                                                        │
│ 5. GitHub Actions executa workflow de notificação            │
│     ↓                                                        │
│ 6. Email enviado para contato@juniorneves.com               │
└─────────────────────────────────────────────────────────────┘
```

## Configurações Necessárias

### GitHub Secrets (SEGURANÇA CRÍTICA)

**⚠️ NUNCA commitar credenciais no código! Use apenas GitHub Secrets.**

#### Configuração Segura no GitHub:

```
Settings → Secrets and variables → Actions → New repository secret
```

| Nome | Valor | Como Gerar |
|------|-------|------------|
| `ZOHO_SMTP_USER` | user@zoho.com | Usuário Zoho Mail |
| `ZOHO_SMTP_PASSWORD` | App Password | Zoho: Configurações → Segurança → Senha de Aplicativo |

#### Por que Zoho Mail?

O e-mail `contato@juniorneves.com` é gerenciado pelo Zoho Mail, que oferece:
- **SMTP/IMAP padrão** com autenticação
- **App Passwords** para aplicações externas
- **Grátis** até 5 usuários e 5GB por usuário
- **Integração** com Google Workspace (se aplicável)

#### Passos para Obter App Password no Zoho:

1. Fazer login em https://accounts.zoho.com/
2. Acessar "Configurações de Segurança"
3. Ativar "Senha de Aplicativo" (se ainda não ativada)
4. Gerar nova senha específica para "GitHub Actions"
5. Copiar e salvar como `ZOHO_SMTP_PASSWORD` no GitHub Secrets

### Permissões Necessárias

- **Actions**: read/write packages
- **Releases**: read/write
- **Pages**: write

## Testes

1. **Teste Manual**
   - Criar release de teste
   - Verificar se email é disparado
   - Confirmar download funcional

2. **Teste Automatizado**
   - Workflow de teste separado
   - Validação de link
   - Verificação de formatação

## Riscos e Mitigações

| Risco | Impacto | Mitigação |
|-------|---------|-----------|
| Email não chega | Médio | Verificar configurações SMTP |
| Download quebrado | Alto | Manter backup local |
| Actions excedem limite | Baixo | Monitorar uso mensal |
| Link quebrado | Médio | Testar antes de publicar |

## Cronograma Estimado

| Etapa | Tempo | Responsável |
|-------|-------|-------------|
| Upload PDF | 5 min | Dev |
| Configurar Actions | 15 min | Dev |
| Atualizar templates | 10 min | Dev |
| Teste | 10 min | Dev |
| Deploy | 5 min | Dev |
| **Total** | **~45 min** | |

## Recursos Adicionais

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Releases Documentation](https://docs.github.com/en/repositories/releasing-releases)
- [dawidd6/action-send-mail](https://github.com/dawidd6/action-send-mail)

## Próximos Passos

1. ✅ APROVADO pelo stakeholder
2. ⏳ Aguardar implementação
3. 🧪 Testar em ambiente de staging
4. 🚀 Deploy para produção
5. 📊 Monitorar downloads e notificações

---

**Arquivo:** `docs/plano-download-github.md`
**Data:** 2026-07-22
**Status:** Para análise