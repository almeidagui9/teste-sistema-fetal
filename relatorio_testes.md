# Relatório de Testes - Sistema de Predição de Saúde Fetal

## Estratégia de Testes

Testes realizados:
- Unitários com Pytest
- Integração com backend + modelo
- Performance com JMeter
- End-to-End com Cypress

## Casos de Teste

| Tipo     | Caso                               | Resultado Esperado | Status |
|----------|------------------------------------|--------------------|--------|
| Unitário | Entrada correta no modelo ML       | Valor entre 1 e 3  | ✅ Passou |
| Integração | POST /registros com dados válidos | Predição + 200 OK | ✅ Passou |
| E2E      | Usuário preenche e vê resultado    | Resultado visível | ✅ Passou |

## Análise de Performance

- 100 requisições simultâneas
- Tempo médio: 240ms
- Taxa de erro: 0%

## Melhorias sugeridas

- Adicionar cache no módulo ML
- Compressão de payload JSON
