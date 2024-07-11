#!/bin/bash

#Alpha Vantage API Key (ersetzen Sie 'YOUR_API_KEY' durch Ihren eigenen Schlüssel)
API_KEY=""

#Funktion zum Abrufen von Aktienkursen
get_stock_price() {
    symbol=$1
    response=$(curl -s "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=$symbol&apikey=$API_KEY")
    price=$(echo "$response" | jq -r '.["Global Quote"]["05. price"]')
    echo "$price"
}

#Funktion zum Abrufen von Bitcoin-Kursen
get_bitcoin_price() {
    response=$(curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    price=$(echo "$response" | jq -r '.bitcoin.usd')
    echo "$price"
}

#Hauptfunktion zur Berechnung des Depotwerts
calculate_portfolio_value() {
    # Angenommene Werte für das Depot
    novartis_amount=10
    nestle_amount=10
    abb_amount=10
    swisscom_amount=10
    usd_amount=3000
    bitcoin_amount=0.1

    # Kosten pro Aktie in CHF (angenommen)
    novartis_cost_per_share=80
    nestle_cost_per_share=100
    # ABB und Swisscom Kosten pro Aktie entsprechend anpassen

    # Aktienkurse abrufen
    novartis_price=$(get_stock_price "NOVN.SW")
    nestle_price=$(get_stock_price "NESN.SW")
    # ABB und Swisscom Kurse entsprechend abrufen

    # Bitcoin-Kurs abrufen
    bitcoin_price=$(get_bitcoin_price)

    # Berechnung des Depotwerts in CHF
    novartis_value=$(echo "scale=2; $novartis_amount * $novartis_price" | bc)
    nestle_value=$(echo "scale=2; $nestle_amount * $nestle_price" | bc)
    # ABB und Swisscom Werte entsprechend berechnen

    usd_value=$usd_amount
    bitcoin_value=$(echo "scale=2; $bitcoin_amount * $bitcoin_price" | bc)

    total_value=$(echo "scale=2; $novartis_value + $nestle_value + $abb_value + $swisscom_value + $usd_value + $bitcoin_value" | bc)
    
    echo "Aktueller Wert des Depots: $total_value CHF"
}

#Hauptprogramm
calculate_portfolio_value

