from graphviz import Digraph
import textwrap
import os

def format_label(text, max_width=30):
    lines = []
    for part in text.split('\n'):
        part = part.strip()
        wrapped_lines = textwrap.wrap(part, max_width)
        lines.extend(wrapped_lines)
    return '\n'.join(lines)

# Erhöhung der DPI-Umgebungseinstellung
os.environ["GRAPHVIZ_DPI"] = "600"

# Erstelle ein gerichtetes Diagramm mit globalen Attributen
dot = Digraph(comment='Baumdiagramm: Rechtfertigung/konfligierende Nachhaltigkeitsaspekte', format='png')

# Diagrammausrichtung von oben nach unten
dot.attr(rankdir='TB')

# Anpassen der Diagrammgröße 
dot.attr(size='6,10!')
dot.attr(ratio='compress')

# Schriftart auf Times New Roman setzen
dot.attr(fontname='Times New Roman')
dot.node_attr.update(fontsize='12', fontname='Times New Roman', shape='box', style='rounded')
dot.edge_attr.update(fontsize='10', fontname='Times New Roman')

# Abstände zwischen den Knoten anpassen
dot.attr(nodesep='0.1', ranksep='0.5')

# Erhöhung der DPI
dot.attr(dpi='600')

# Knoten definieren
dot.node('S1', format_label('Rechtfertigung/\nkonfligierende Nachhaltigkeitsaspekte', 25))

dot.node('S2a', format_label('Genereller Ausschluss einer Berücksichtigung von\n(bestimmten) Nachhaltigkeitsaspekten', 25))
dot.node('S2b', format_label('Abwägung', 25))
dot.node('S2c', format_label('Genereller Vorrang von\n(bestimmten) Nachhaltigkeitsaspekten', 25))

dot.node('S3a', format_label('Quantifizierung', 25))
dot.node('S3b', format_label('Alternative Abwägungsmetrik', 25))
dot.node('S3c', format_label('Herstellung praktischer Konkordanz', 25))

# Kanten definieren
dot.edge('S1', 'S2a')
dot.edge('S1', 'S2b')
dot.edge('S1', 'S2c')

dot.edge('S2b', 'S3a')
dot.edge('S2b', 'S3b')
dot.edge('S2b', 'S3c')

# Knoten auf derselben Höhe gruppieren
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('S2a')
    s.node('S2b')
    s.node('S2c')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('S3a')
    s.node('S3b')
    s.node('S3c')

# Diagramm rendern und anzeigen
dot.render('zweiter_baum', view=True)
