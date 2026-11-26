import csv
import sys
from pathlib import Path
from statistics import mean
import matplotlib.pyplot as plt

base = Path(__file__).resolve().parent
fonte = Path(sys.argv[1]) if len(sys.argv) > 1 else base / 'dados/resultados.csv'
with fonte.open(encoding='utf-8') as f:
    linhas = list(csv.DictReader(f))
sem = [float(r['sem_fsync_ms']) for r in linhas]
com = [float(r['com_fsync_ms']) for r in linhas]
medias = [mean(sem), mean(com)]
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.bar([0, 1], medias, width=.48, alpha=.55, label='Média')
for i, valores in enumerate([sem, com]):
    ax.scatter([i + (j-(len(valores)-1)/2)*.055 for j in range(len(valores))], valores, color='black', zorder=3, label='Rodadas individuais' if i == 0 else None)
    ax.text(i, max(valores)+4, f'Média: {medias[i]:.4f} ms', ha='center', fontsize=11)
ax.axhline(medias[0], linestyle='--', color='gray', label='Referência: média sem fsync')
ax.set_xticks([0,1], ['Sem fsync', 'Com fsync após cada registro'])
ax.set_xlabel('Condição de gravação')
ax.set_ylabel('Tempo total (ms)')
ax.set_ylim(0, max(com+sem)*1.22)
ax.set_title(f'Com fsync, o tempo médio foi {medias[1]/medias[0]:.1f} vezes maior\n100 registros por condição', fontsize=14)
ax.legend(loc='upper left', fontsize=9)
ax.grid(axis='y', alpha=.2)
fig.tight_layout()
fig.savefig(base / 'grafico.png', dpi=180)
