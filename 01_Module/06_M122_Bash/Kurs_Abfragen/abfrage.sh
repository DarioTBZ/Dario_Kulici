#!/bin/bash

API_KEY="bc5a975b90e7226110a23875"
API_URL="https://v6.exchangerate-api.com/v6//latest/CHF"
DATA_FILE="exchange_data.json"

# Funktion zum Abrufen der aktuellen Wechselkurse
get_exchange_rates() {
    response=$(curl -s "$API_URL")
    echo "$response"
}

# Funktion zum Laden der alten Daten
load_old_data() {
    if [ -f "$DATA_FILE" ]; then
        cat "$DATA_FILE"
    else
        echo "{}"
    fi
}

# Funktion zum Speichern der neuen Daten
save_new_data() {
    echo "$1" > "$DATA_FILE"
}

# Funktion zur Berechnung der Differenz und Darstellung der Daten
compare_and_display() {
    old_data=$(load_old_data)
    new_data="$1"

    echo "Währungen: CHF zu EUR, USD, ETH, BTC, GBP, JPY"
    echo "-----------------------------------------------"

    for currency in EUR USD ETH BTC GBP JPY; do
        old_rate=$(echo "$old_data" | jq -r ".conversion_rates.$currency // 0")
        new_rate=$(echo "$new_data" | jq -r ".conversion_rates.$currency")
        
        if [ "$(echo "$old_rate > 0" | bc)" -eq 1 ]; then
            diff=$(echo "scale=6; $new_rate - $old_rate" | bc)
            percent_change=$(echo "scale=2; ($diff / $old_rate) * 100" | bc)

            if [ "$(echo "$diff > 0" | bc)" -eq 1 ]; then
                color="\033[32m"  # grün
                change="↑"
            else
                color="\033[31m"  # rot
                change="↓"
            fi

            printf "%-10s: %-10s -> %-10s (%s%.4f%%\033[0m)\n" "$currency" "$old_rate" "$new_rate" "$color" "$percent_change"
        else
            printf "%-10s: %-10s -> %-10s\n" "$currency" "N/A" "$new_rate"
        fi
    done
}

# Hauptskript
new_data=$(get_exchange_rates)

if [ -n "$new_data" ]; then
    compare_and_display "$new_data"
    save_new_data "$new_data"
else
    echo "Fehler beim Abrufen der Wechselkurse."
fi

