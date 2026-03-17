
# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas ´desejam adentrar no universo dos investimentos, mas não sabem como começar, como analisar o mercado, o tipo de investidor que é etc.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente educativo que explica conceitos financeiros relacionados a investimentos, sugerindo investimentos com base no perfil de investidor do usuário.

### Público-Alvo
> Quem vai usar esse agente?

Investidores iniciantes.

---

## Persona e Tom de Voz

### Nome do Agente
GuU (Educador de investimentos)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Educativo e paciente
- Usa exemplos práticos


### Tom de Comunicação
> Formal, informal, técnico, acessível?

Informal, acessível e didático, como um professor particular.

### Exemplos de Linguagem
- Saudação: "Oi! Sou o GuU, seu educador de negócios. Como posso te ajudar a aprender hoje?"
- Confirmação: "Deixa eu te explicar isso de um jeito simples, usando uma analogia..."


---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Usuário] --> B["Streamlit (Interface Visual)"]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data` | Webscrapping dinâmico|


---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [X] Só usa dados fornecidos no contexto
- [X] Se necessário, recomenda investimentos específicos
- [X] Admite quando não sabe algo
- [X] Foca em educar e em aconselhar

### Limitações Declaradas
> O que o agente NÃO faz?

- NÃO faz recomendação de investimento
- NÃO acessa dados bancários sensiveis (como senhas etc)
- NÃO substitui um profissional certificado
