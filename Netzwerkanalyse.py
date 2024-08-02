import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Pfad zur Excel-Datei
file_path = '/filde_path/interlinkages_database_adv_search.xlsx'

# Laden der Excel-Datei
df = pd.read_excel(file_path, sheet_name='database_adv_search')

# Definieren der Farben für jedes SDG basierend auf den UN-Farben
sdg_colors = {
    1: '#E5243B',  # SDG 1: No Poverty
    2: '#DDA63A',  # SDG 2: Zero Hunger
    3: '#4C9F38',  # SDG 3: Good Health and Well-being
    4: '#C5192D',  # SDG 4: Quality Education
    5: '#FF3A21',  # SDG 5: Gender Equality
    6: '#26BDE2',  # SDG 6: Clean Water and Sanitation
    7: '#FCC30B',  # SDG 7: Affordable and Clean Energy
    8: '#A21942',  # SDG 8: Decent Work and Economic Growth
    9: '#FD6925',  # SDG 9: Industry, Innovation, and Infrastructure
    10: '#DD1367', # SDG 10: Reduced Inequality
    11: '#FD9D24', # SDG 11: Sustainable Cities and Communities
    12: '#BF8B2E', # SDG 12: Responsible Consumption and Production
    13: '#3F7E44', # SDG 13: Climate Action
    14: '#0A97D9', # SDG 14: Life Below Water
    15: '#56C02B', # SDG 15: Life on Land
    16: '#00689D', # SDG 16: Peace and Justice Strong Institutions
    17: '#19486A'  # SDG 17: Partnerships to achieve the Goal
}

# Erstellen der Graphen
G_synergy = nx.Graph()
G_tradeoff = nx.Graph()

# Kanten mit Gewichten basierend auf der Anzahl der Interaktionen hinzufügen, getrennt für Synergy und Trade-off
for _, row in df.iterrows():
    if row['Type'] == 'synergy':
        if G_synergy.has_edge(row['GoalA'], row['GoalB']):
            G_synergy[row['GoalA']][row['GoalB']]['weight'] += 1
        else:
            G_synergy.add_edge(row['GoalA'], row['GoalB'], weight=1)
    elif row['Type'] == 'trade-off':
        if G_tradeoff.has_edge(row['GoalA'], row['GoalB']):
            G_tradeoff[row['GoalA']][row['GoalB']]['weight'] += 1
        else:
            G_tradeoff.add_edge(row['GoalA'], row['GoalB'], weight=1)

# Gewichte für Knoten basierend auf der Anzahl der Interaktionen berechnen
node_weights = df['GoalA'].value_counts() + df['GoalB'].value_counts()

# Farben für die Knoten generieren
node_colors = [sdg_colors[node] for node in G_synergy.nodes()]

# Netzwerk mit circular layout zeichnen
pos = nx.circular_layout(G_synergy, scale=3)

plt.figure(figsize=(12, 12))

# Zeichnen des Synergy-Graphen
nx.draw_networkx_nodes(G_synergy, pos, node_size=[1.25 * node_weights.get(node, 1) for node in G_synergy.nodes()], node_color=node_colors)
nx.draw_networkx_edges(G_synergy, pos, width=[0.02 * G_synergy[u][v]['weight'] for u, v in G_synergy.edges()], edge_color='#b7d5ac')

# Zeichnen des Trade-off-Graphen
nx.draw_networkx_edges(G_tradeoff, pos, width=[0.02 * G_tradeoff[u][v]['weight'] for u, v in G_tradeoff.edges()], edge_color='#ff7d82', style='dashed')

plt.title('Übereinandergelegte SDG-Interaktionen (Synergien in hellgrün, Trade-offs in hellrot)')
plt.show()
