#!/bin/bash

# Initiale Depot-Konfiguration
depot=("Novartis" 10 "Nestle" 10 "ABB" 10 "Swiscom" 10 "USD" 3000 "Bitcoin" 0.1)
kaufpreise=("Novartis" 80 "Nestle" 100 "ABB" 30 "Swiscom" 60 "USD" 0.95 "Bitcoin" 30000)

# API URLs
STOCK_API="https://query1.finance.yahoo.com/v7/finance/quote?symbols="
FOREX_API="https://api.exchangerate-api.com/v4/latest/USD"
CRYPTO_API="https://api.coindesk.com/v1/bpi/currentprice/BTC.json"

# Funktionsdefinitionen
get_stock_price() {
    stock=$1
    symbol=$2
    price=$(curl -s "${STOCK_API}${symbol}" | jq -r '.quoteResponse.result[0].regularMarketPrice')
    if [[ -z "$price" ]]; then
        echo "Error: Failed to get price for $stock"
        price=0
    fi
    echo "$price"
}

get_forex_rate() {
    rate=$(curl -s "${FOREX_API}" | jq -r '.rates.CHF')
    if [[ -z "$rate" ]]; then
        echo "Error: Failed to get forex rate"
        rate=0
    fi
    echo "$rate"
}

get_crypto_price() {
    price=$(curl -s "${CRYPTO_API}" | jq -r '.bpi.USD.rate_float')
    if [[ -z "$price" ]]; then
        echo "Error: Failed to get crypto price"
        price=0
    fi
    echo "$price"
}

# Aktuelle Kurse abfragen
novartis_price=$(get_stock_price "Novartis" "NOVN.SW")
nestle_price=$(get_stock_price "Nestle" "NESN.SW")
abb_price=$(get_stock_price "ABB" "ABBN.SW")
swiscom_price=$(get_stock_price "Swiscom" "SCMN.SW")
usd_to_chf=$(get_forex_rate)
bitcoin_price=$(get_crypto_price)

# Debug-Ausgaben der Preise
echo "Novartis price: $novartis_price"
echo "Nestle price: $nestle_price"
echo "ABB price: $abb_price"
echo "Swiscom price: $swiscom_price"
echo "USD to CHF rate: $usd_to_chf"
echo "Bitcoin price: $bitcoin_price"

# Aktuellen Depotwert berechnen
depot_wert_chf=0
for ((i=0; i<${#depot[@]}; i+=2)); do
    asset=${depot[i]}
    menge=${depot[i+1]}
    case $asset in
        "Novartis")
            wert=$(echo "$novartis_price * $menge" | bc)
            ;;
        "Nestle")
            wert=$(echo "$nestle_price * $menge" | bc)
            ;;
        "ABB")
            wert=$(echo "$abb_price * $menge" | bc)
            ;;
        "Swiscom")
            wert=$(echo "$swiscom_price * $menge" | bc)
            ;;
        "USD")
            wert=$(echo "$usd_to_chf * $menge" | bc)
            ;;
        "Bitcoin")
            wert=$(echo "$bitcoin_price * $menge" | bc)
            ;;
        *)
            wert=0
            ;;
    esac
    depot_wert_chf=$(echo "$depot_wert_chf + $wert" | bc)
done

# Historischen Wert berechnen (Einkaufspreis)
historischer_wert=0
for ((i=0; i<${#kaufpreise[@]}; i+=2)); do
    asset=${kaufpreise[i]}
    preis=${kaufpreise[i+1]}
    for ((j=0; j<${#depot[@]}; j+=2)); do
        if [ "$asset" == "${depot[j]}" ]; then
            menge=${depot[j+1]}
            wert=$(echo "$preis * $menge" | bc)
            historischer_wert=$(echo "$historischer_wert + $wert" | bc)
        fi
    done
done

# Differenz in %
differenz=$(echo "scale=2; ($depot_wert_chf - $historischer_wert) / $historischer_wert * 100" | bc)

# Ergebnis ausgeben und speichern
timestamp=$(date +'%Y-%m-%d %H:%M:%S')
echo "$timestamp: Depotwert: CHF $depot_wert_chf, Historischer Wert: CHF $historischer_wert, Differenz: $differenz%" | tee -a depot_verlauf.txt

