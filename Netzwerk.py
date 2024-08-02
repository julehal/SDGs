import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Pfad zur Excel-Datei
file_path = '/file_path/interlinkages_database_adv_search.xlsx'

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

# Erstellen des MultiGraphen
G = nx.MultiGraph()

# Kanten mit Gewichten basierend auf der Anzahl der Interaktionen hinzufügen für Synergy und Trade-off
for _, row in df.iterrows():
    if row['Type'] in ['synergy', 'trade-off']:
        if G.has_edge(row['GoalA'], row['GoalB']):
            # Prüfen, ob es bereits eine Kante vom gleichen Typ gibt
            edge_exists = False
            for key, attr in G[row['GoalA']][row['GoalB']].items():
                if attr['type'] == row['Type']:
                    G[row['GoalA']][row['GoalB']][key]['weight'] += 1
                    edge_exists = True
                    break
            if not edge_exists:
                G.add_edge(row['GoalA'], row['GoalB'], weight=1, type=row['Type'])
        else:
            G.add_edge(row['GoalA'], row['GoalB'], weight=1, type=row['Type'])

# Gewichte für Knoten basierend auf der Anzahl der Interaktionen berechnen
node_weights = df['GoalA'].value_counts() + df['GoalB'].value_counts()

# Farben für die Knoten generieren
node_colors = [sdg_colors[node] for node in G.nodes()]

# Farben für die Kanten basierend auf dem Interaktionstyp zuweisen
edge_colors = []
edge_weights = []
for u, v, keys, data in G.edges(data=True, keys=True):
    if data['type'] == 'synergy':
        edge_colors.append('#b7d5ac')  # hellgrün für Synergien
    elif data['type'] == 'trade-off':
        edge_colors.append('#ff7d82')  # hellrot für Trade-offs
    edge_weights.append(data['weight'])

# Netzwerk mit circular layout, gewichteten Knoten und farbigen Kanten zeichnen
plt.figure(figsize=(12, 12))
pos = nx.circular_layout(G, scale=3)

# Knoten mit spezifizierten Farben zeichnen
nx.draw_networkx_nodes(G, pos, node_size=[1.25 * node_weights.get(node, 1) for node in G.nodes()], node_color=node_colors)
# Kanten mit spezifizierten Farben zeichnen
nx.draw_networkx_edges(G, pos, width=[0.02 * w for w in edge_weights], edge_color=edge_colors)
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title('Netzwerkanalyse der SDG-Interaktionen (Circular Layout, farbige Knoten und Kanten für Synergien und Trade-offs)')
plt.show()
