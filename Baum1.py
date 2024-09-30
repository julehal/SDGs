from graphviz import Digraph
import textwrap
import os

def format_label(text, max_width=20):
    lines = []
    for part in text.split('\n'):
        part = part.strip()
        if part.startswith('-'):
            # Zeile beginnt mit einem Gedankenstrich
            wrapped_lines = textwrap.wrap(part, max_width, subsequent_indent='  ')
            lines.extend(wrapped_lines)
        else:
            # Normale Zeile
            wrapped_lines = textwrap.wrap(part, max_width)
            lines.extend(wrapped_lines)
    return '\n'.join(lines)

# Erhöhung der DPI-Umgebungseinstellung 
os.environ["GRAPHVIZ_DPI"] = "600"

# Erstelle ein gerichtetes Diagramm mit globalen Attributen
dot = Digraph(comment='Erster Baum: Nachhaltigkeitsaspekte und Wettbewerbsrecht', format='pdf')

# Diagrammausrichtung von oben nach unten
dot.attr(rankdir='TB')

# Anpassen der Diagrammgröße
dot.attr(size='5,30!')
dot.attr(ratio='compress')

# Schriftart auf Times New Roman setzen
dot.attr(fontname='Times New Roman')
dot.node_attr.update(fontsize='10', fontname='Times New Roman', shape='box', style='rounded')
dot.edge_attr.update(fontsize='9', fontname='Times New Roman')

# Abstände zwischen den Knoten anpassen 
dot.attr(nodesep='0.05', ranksep='0.7')

# Erhöhung der DPI
dot.attr(dpi='600')

# Knoten definieren 
dot.node('1', format_label('Nachhaltigkeits-\naspekte und\nWettbewerbsrecht', 22))

dot.node('2a', format_label('Nachhaltigkeitsaspekt als\nWettbewerbsparameter\n(Wettbewerbsimmanenz)', 28))
dot.node('2b', format_label('Nachhaltigkeitsaspekt als\naußerwettbewerbliches Ziel', 26))

dot.node('3a', format_label('Nachhaltigkeitsaspekt im\nEinklang mit\nWettbewerbsrecht', 26))
dot.node('3b', format_label('Zielkonflikt zwischen\nNachhaltigkeitsaspekt und\nWettbewerbsrecht', 26))

dot.node('4a', format_label('Sensibilisierung notwendig\n(gesetzliche Regelung\nzusätzlich möglich,\naber nicht notwendig)', 22))

dot.node('4b', format_label('Keine Berücksichtigungs-\nfähigkeit außerwettbewerb-\nlicher Ziele', 22))
dot.node('4c', format_label('Nachhaltigkeitsaspekte\nsind berücksichtigungs-fähig, aber ...', 22))
dot.node('4d', format_label('Generelle Berücksichtigungs-\nfähigkeit von\nNachhaltigkeitsaspekten', 24))

dot.node('5a', format_label('Gesetzliche Regelung\nnotwendig', 22))
dot.node('5b', format_label('Regelung in Guidelines\nder Kommission\nnotwendig', 22))
dot.node('5c', format_label('Abwägung im Einzelfall\nnotwendig', 22))

# Kanten definieren
dot.edge('1', '2a')
dot.edge('1', '2b')

dot.edge('2a', '4a')

dot.edge('2b', '3a')
dot.edge('2b', '3b')

dot.edge('3a', '4a')

dot.edge('3b', '4b')
dot.edge('3b', '4c')
dot.edge('3b', '4d')

dot.edge('4c', '5a')
dot.edge('4c', '5b')
dot.edge('4c', '5c')

# Knoten auf derselben Höhe gruppieren
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('4b')
    s.node('4c')
    s.node('4d')

with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('5a')
    s.node('5b')
    s.node('5c')

# Diagramm rendern und anzeigen
dot.render('erster_baum', view=True)
