#!/bin/bash

# Log-Datei
LOGFILE="download_log.txt"

# Loggen
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOGFILE"
}

# Funktion installieren
install_game() {
    local package=$1
    local game_name=$2
    if brew list --formula | grep -q "^$package\$"; then
        log "$game_name ist bereits installiert."
        echo "$game_name ist bereits installiert."
    else
        read -p "Möchten Sie $game_name installieren? (j/n): " answer
        if [[ $answer == "j" || $answer == "J" ]]; then
            log "Installation von $game_name gestartet."
            brew install $package
            if [[ $? -eq 0 ]]; then
                log "$game_name erfolgreich installiert."
            else
                log "Fehler bei der Installation von $game_name."
            fi
        else
            log "$game_name wurde nicht installiert."
        fi
    fi
}

# Überprüfen, ob Homebrew installiert ist
if ! command -v brew &> /dev/null; then
    echo "Homebrew ist nicht installiert. Bitte installieren Sie Homebrew zuerst."
    exit 1
fi

# Update Homebrew
log "Aktualisieren von Homebrew gestartet."
brew update
if [[ $? -eq 0 ]]; then
    log "Homebrew erfolgreich aktualisiert."
else
    log "Fehler beim Aktualisieren von Homebrew."
fi

# Spiel 1: c2048
install_game "c2048" "2048 CLI (c2048)"

# Spiel 2: moon-buggy
install_game "moon-buggy" "Moon Buggy"

# Spiel 3: ninvaders
install_game "ninvaders" "Space Invaders (ninvaders)"

log "Skript abgeschlossen."
echo "Alle Aufgaben abgeschlossen. Details siehe $LOGFILE"

