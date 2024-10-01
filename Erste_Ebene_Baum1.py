from graphviz import Digraph
import textwrap
import os

def format_label(text, max_width=25):
    lines = []
    for part in text.split('\n'):
        part = part.strip()
        wrapped_lines = textwrap.wrap(part, max_width)
        lines.extend(wrapped_lines)
    return '\n'.join(lines)

# Erhöhung der DPI-Umgebungseinstellung 
os.environ["GRAPHVIZ_DPI"] = "600"

# Erstelle ein gerichtetes Diagramm mit globalen Attributen
dot = Digraph(comment='Erster Baum: Nachhaltigkeitsaspekte und Wettbewerbsrecht', format='pdf')

# Diagrammausrichtung von oben nach unten
dot.attr(rankdir='TB')

# Anpassung der Diagrammgröße
dot.attr(size='5,15!')
dot.attr(ratio='compress')

# Schriftart auf Times New Roman setzen
dot.attr(fontname='Times New Roman')
dot.node_attr.update(fontsize='10', fontname='Times New Roman', shape='box', style='rounded')
dot.edge_attr.update(fontsize='9', fontname='Times New Roman')

# Abstände zwischen den Knoten anpassen 
dot.attr(nodesep='0.05', ranksep='0.7')

# Erhöhung der DPI
dot.attr(dpi='600')

####################
# Erster Baum (nur Ebenen 1 und 2)
####################

# Knoten definieren mit angepassten Labels
dot.node('1', format_label('Nachhaltigkeits-\naspekte und\nWettbewerbsrecht', 22))

dot.node('2a', format_label('Nachhaltigkeitsaspekt als\nWettbewerbsparameter\n(Wettbewerbsimmanenz)', 28))
dot.node('2b', format_label('Nachhaltigkeitsaspekt als\naußerwettbewerbliches Ziel', 26))

# Kanten definieren
dot.edge('1', '2a')
dot.edge('1', '2b')

# Diagramm rendern und anzeigen
dot.render('erster_baum', view=True)
