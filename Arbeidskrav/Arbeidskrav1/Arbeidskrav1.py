# Input for antall kilometer
km = int(input("Hvor mange kilometer kjører du per år?: "))

# Trafikkforsikring. Antar 365 dager i året
trafikkforsikring = 8.38*365 

# Kostnader relatert til elbil
forsikring_el = 5000 #Forsikring fastpris per år
strompris = 2 # Strømpris på 2 kr/kWh
forbruk_km_el = 0.2 * strompris
bomavgift_km_el = 0.1 #Bomavgift per kilometer elbil

totalkostnad_el = forsikring_el + trafikkforsikring + (forbruk_km_el + bomavgift_km_el) * km

# Kostnader relatert til bensinbil
forsikring_bensin = 7500 #Forsikring fastpris per år
forbruk_km_bensin = 1
bomavgift_km_bensin = 0.3 #Bomavgift per kilometer bensin

totalkostnad_bensin = forsikring_bensin + trafikkforsikring + (forbruk_km_bensin + bomavgift_km_bensin) * km

# En sjekk for å undersøke om kostnaden for bensinbil er høyere enn elbil. Utfallet avgjør hvilken tekst som skrives ut.
if totalkostnad_bensin > totalkostnad_el:
    print(f"Totalkostnaden for å kjøre {km} kilometer er {totalkostnad_el} kroner for elbil og {totalkostnad_bensin} kroner for bensinbil. Det er {totalkostnad_bensin - totalkostnad_el} kroner dyrere å kjøre bensinbil.") 
else:
    print(f"Totalkostnaden for å kjøre {km} kilometer er {totalkostnad_el} kroner for elbil og {totalkostnad_bensin} kroner for bensinbil. Det er {totalkostnad_el - totalkostnad_bensin} kroner dyrere å kjøre elbil.")