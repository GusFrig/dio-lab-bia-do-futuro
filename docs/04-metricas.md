



## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Pergunta de conceito
- **Pergunta:** "explique o principal conceito do investimento para quem está iniciando na área"
- **Resposta esperada:** "Investir, de um jeito muito simples, significa colocar o seu dinheiro para trabalhar para você"
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Pergunta fora do escopo
- **Pergunta:** "Que dia é hoje?"
- **Resposta esperada:** "Olá! Eu sou o GuU, seu educador financeiro amigável e, por regra, jamais respondo a perguntas que fujam do tema de investimentos, como informar que dia é hoje
. O meu papel é focar exclusivamente em te ensinar sobre o mundo das finanças"
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Informação inexistente
- **Pergunta:** "Qual a valorização do mxrf11 para o dia 19/03/2026?"
- **Resposta esperada:** "As fontes que tenho disponíveis não contêm informações sobre a valorização ou cotação específica do ativo MXRF11 para a data de hoje (19/03/2026)." 
- **Resultado:** [X] Correto  [ ] Incorreto

---

## Formulário de Feedback (Sugestão)

Use com os participantes do teste:

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "As respostas responderam suas perguntas?" | ___ |
| Segurança | "As informações pareceram confiáveis?" | ___ |
| Coerência | "A linguagem foi clara e fácil de entender?" | ___ |

**Comentário aberto:** O que você achou desta experiência e o que poderia melhorar?

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]
