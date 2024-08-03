import matplotlib.pyplot as plt
import numpy as np

# Parameter für exponentielles Wachstum
initial_value = 1000  # Anfangswert des BIP
growth_rate = 0.15    # Höhere Wachstumsrate für stärkere Krümmung
time_periods = np.arange(0, 21, 1)  # Zeit von 0 bis 20 Jahren

# Berechnung des exponentiellen Wachstums
bip_values = initial_value * np.exp(growth_rate * time_periods)

# Erstellen des Plots ohne Skalen
plt.figure(figsize=(10, 6))
plt.plot(time_periods, bip_values, label='Exponentielles Wachstum', color='blue')

# Beschriftungen und Titel
plt.xlabel('Zeit')
plt.ylabel('BIP')
plt.title('Exponentielles Wachstum des BIP über die Zeit')
plt.legend()

# Entfernen der Skalen
plt.xticks([])
plt.yticks([])

# Grenzen der x-Achse und y-Achse setzen
plt.xlim(left=0)  # x-Achse beginnt bei 0
plt.ylim(bottom=0)  # y-Achse beginnt bei 0

# Plot anzeigen
plt.show()
