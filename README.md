# Projeto 2 — Custo da persistência

## Executar
No terminal do VS Code, dentro da pasta do projeto:

```powershell
python medir_fsync.py
python -m pip install matplotlib
python gerar_grafico.py
```
O primeiro comando cria um CSV novo com data e hora em dados/. O gráfico padrão usa dados/resultados.csv, transcrito da medição original. Para gerar gráfico de uma nova execução, passe o caminho do novo CSV como argumento: `python gerar_grafico.py dados/medicao_...csv` (substitua pelo nome real). Isso substitui grafico.png; o PDF permanece com os dados originais.

## Antes de entregar
- Confirmar hipótese original e contribuições de cada integrante; completar relatório e especificações do dispositivo.
- Conferir CSV com a saída original do terminal; anexar a captura ou arquivo original e o script original, se disponível.
- Revisar declaração de IA e confirmar se o professor permite assistência na elaboração do código e relatório.
- Criar repositório público no GitHub, enviar arquivos e colar link na ficha. Não publicar credenciais ou RA.
- Preencher a ficha individual com a hipótese real e a ficha de grupo com os cinco valores por condição.

O script atualizado exporta novas medições, não reproduz artificialmente os tempos históricos.
