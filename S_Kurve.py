import matplotlib.pyplot as plt
import numpy as np

# Parameter für die S-Kurve des Wachstums (logistisches Wachstum)
initial_value = 5  # Anfangswert des BIP
carrying_capacity = 1000  # Kapazitätsgrenze
growth_rate = 0.6  # Wachstumsrate für eine deutliche S-Kurve
time_periods = np.arange(0, 18, 0.1)  # Zeitverlauf

# Berechnung des S-förmigen Wachstums (logistische Funktion)
bip_values = carrying_capacity / (1 + (carrying_capacity / initial_value - 1) * np.exp(-growth_rate * time_periods))

# Erstellen des Plots ohne Skalen
plt.figure(figsize=(10, 6))
plt.plot(time_periods, bip_values, label='S-Kurve des Wachstums', color='green')

# Beschriftungen und Titel
plt.xlabel('Zeit')
plt.ylabel('BIP')
plt.title('S-Kurve des Wachstums des BIP über die Zeit')
plt.legend()

# Entfernen der Skalen
plt.xticks([])
plt.yticks([])

# Grenzen der x-Achse und y-Achse setzen
plt.xlim(left=0)  # x-Achse beginnt bei 0
plt.ylim(bottom=0)  # y-Achse beginnt bei 0

# Plot anzeigen
plt.show()
