# Segurança do Repositório GitHub

## Status Atual

**Branch `main` não está protegido**

Mensagem do GitHub:
> "Your main branch isn't protected. Protect this branch from force pushing or deletion, or require status checks before merging."

## O que significa

- **Branch não protegido** = qualquer um pode fazer push force ou deletar o branch
- **Risco de perda** = código pode ser sobrescrito ou excluído acidentalmente
- **Sem status checks** = Pull Requests não precisam passar por testes antes de mergear

## Riscos Associados

| Risco | Impacto | Probabilidade |
|-------|---------|---------------|
| Push force acidental | Perda de código | Médio |
| Deletar branch | Perda total de histórico | Baixo |
| Merge sem revisão | Código não testado | Médio |
| Alterações não testadas | Bugs em produção | Médio |

## Recomendações de Segurança

### 1. Proteger o Branch Principal

**Configuração:**
```
Settings → Branches → Add rule
Branch name: main
```

**Opções recomendadas:**
- ✅ Require a pull request before merging
- ✅ Require approvals (1 reviewer mínimo)
- ✅ Require status checks to pass before merging
- ✅ Require linear history
- ✅ Include administrators
- ❌ Allow force pushes
- ❌ Allow deletions

### 2. Configurar Status Checks

Status checks obrigatórios:
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Linting (ruff, eslint, etc.)
- [ ] Testes unitários
- [ ] Validação de segurança (trivy, bandit)

### 3. Proteção de Secrets

- [ ] Nunca commitar credenciais
- [ ] Usar GitHub Secrets
- [ ] Rotacionar secrets periodicamente
- [ ] Revisar permissões de secrets

### 4. Revisão de Código

- [ ] Pull Requests obrigatórios
- [ ] Mínimo 1 reviewer
- [ ] Reviews assinados (quando possível)
- [ ] Linter automático em PRs

### 5. Monitoramento

- [ ] Enable GitHub Advanced Security (se disponível)
- [ ] Monitorar alerts de segurança
- [ ] Revisar logs de acesso regularmente

## Ações Imediatas

1. ✅ **Documentado** - Este arquivo criado
2. ⏳ **Pendente** - Habilitar branch protection
3. ⏳ **Pendente** - Configurar status checks
4. ⏳ **Pendente** - Revisar permissões de colaboradores

## Referências

- [GitHub Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-protected-branches)
- [GitHub Security](https://docs.github.com/en/code-security)

---

**Arquivo:** `docs/seguranca-repositorio-github.md`
**Data:** 2026-07-22
**Status:** Análise concluída, ações pendentes