import matplotlib.pyplot as plt
import numpy as np

# Erstellen der Daten für die Kuznets-Kurve
x = np.linspace(0, 100, 500)  # Pro-Kopf-Einkommen
y = -0.002 * (x - 50) ** 2 + 5  # Krümmung für die Ungleichheit

# Plotten der Kuznets-Kurve
plt.figure(figsize=(10, 6))
plt.plot(x, y, label="Kuznets-Kurve", color="blue")

# Achsenbeschriftungen und Titel
plt.xlabel("Pro-Kopf-Einkommen")
plt.ylabel("Ungleichheit")
plt.title("Kuznets-Kurve (umgedrehtes U)")
plt.grid(False)

# Entfernen der Skalen an den Seiten
plt.xticks([])
plt.yticks([])

# Entfernen der zusätzlichen Linien
plt.axhline(0, color='white', linewidth=0)
plt.axvline(0, color='white', linewidth=0)

# Anzeigen der Legende
plt.legend()

# Anzeige des Plots
plt.show()
