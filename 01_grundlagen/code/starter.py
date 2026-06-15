"""
Baustein 01 – Grundlagen der Softwaretests
Startvorlage – bearbeite diese Datei für deine Aufgaben.
"""


# ============================================================
# Aufgabe 1 – Fehlerhafte Funktion
# ============================================================

def berechne_rabatt(preis: float, prozent: float) -> float:
    """
    Berechnet den Preis nach Rabattabzug.

    Beispiel:
        berechne_rabatt(100.0, 20) soll 80.0 zurückgeben.
    """
    # Hier ist ein Defekt eingebaut – findest du ihn?
    rabatt = preis * prozent  # <-- Zeile mit Defekt
    return preis - rabatt


# Aufgabe 1a): Beantworte folgende Fragen als Kommentar:

# Error (falsche Handlung des Entwicklers):
# TODO: Deine Antwort hier 
#Der Entwickler hat den Rabatt falsch berechnet, indem er den Prozentsatz direkt mit dem Preis multipliziert hat, anstatt den Prozentsatz durch 100 zu teilen.

# Defect (fehlerhafte Stelle im Code):
# TODO: Deine Antwort hier
#Der Defekt ist in Zeile 19 wp preis * prozent genommen wird.

# Failure (was der Benutzer bemerken würde):
# TODO: Deine Antwort hier
#Der Rabat wird viel zu hoch berechnet, der Preis stimmt am ende nicht


# Aufgabe 1b): Korrigiere die Funktion unten und füge print()-Tests hinzu.

def berechne_rabatt_korrigiert(preis: float, prozent: float) -> float:
    """
    Korrigierte Version von berechne_rabatt().
    TODO: Implementiere die korrekte Logik.
    """
    pass  # TODO: Ersetze 'pass' durch deine Implementierung


# Manuelle Tests (werden in Baustein 05 durch echte Unit-Tests ersetzt)
if __name__ == "__main__":
    # TODO: Ergänze mindestens 3 eigene print()-Tests für berechne_rabatt_korrigiert().
    # Überlege selbst: Was sind sinnvolle Eingaben? Was erwartest du als Ergebnis?

    print("=== Test: berechne_rabatt (fehlerhaft) ===")
    print(berechne_rabatt(100.0, 20))  # Falsche Ausgabe erwartet

    print("\n=== Test: berechne_rabatt_korrigiert ===")
    # TODO: Deine Tests hier
    if berechne_rabatt_korrigiert(100.0, 20) == 80.0:
        print("Test 1 bestanden")
    else:
        print("Test 1 fehlgeschlagen. Erwartetes Ergebnis: 80.0, tatsächliches Ergebnis:", berechne_rabatt_korrigiert(100.0, 20))

    if berechne_rabatt_korrigiert(64.0, 30) == 44.8:
        print("Test 2 bestanden")
    else:
        print("Test 2 fehlgeschlagen. Erwartetes Ergebnis: 44.8, tatsächliches Ergebnis:", berechne_rabatt_korrigiert(64.0, 30))


# ============================================================
# Aufgabe 2 – Statisch vs. dynamisch
# ============================================================

# Trage hier deine ausgefüllte Tabelle als Kommentar ein:
#
# | Maßnahme                            | Statisch | Dynamisch |
# |-------------------------------------|----------|-----------|
# | Code Review durch einen Kollegen    | X        |           |
# | Programm mit Testdaten ausführen    |          | X         |
# | Syntaxprüfung durch den Editor      | X        |           |
# | Walkthroughs im Team                | X        |           |
# | Unit-Tests laufen lassen            |          | X         |
# | Checklisten für Codestruktur        | X        |           |
#
# Warum reicht statisches Testen allein nicht aus?
# TODO: Deine Erklärung hier (2 Sätze)
# Statische Tests dauern oft länger, da sie manuell durchgeführt werden müssen. Außerdem können nicht alle Fehler gefunden werden wenn das Programm nicht ausgeführt wird.


# ============================================================
# Aufgabe 3 – Grundprinzipien (Antworten als Kommentar)
# ============================================================

# Prinzip 2 – Vollständiges Testen ist unmöglich:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier
# Es gibt unendlich viele mögliche Eingaben, Kombinationen und Pfade in einem Programm, daher ist es unmöglich, alle möglichen Szenarien zu testen.

# Prinzip 4 – Defect Clustering:
# Beispiel aus dem Berufsalltag:
# TODO: Deine Antwort hier
# In einem Softwareprojekt treten Fehler oft in bestimmten Modulen oder Komponenten auf, während andere Teile des Codes relativ fehlerfrei bleiben. Zum Beispiel könnte ein bestimmtes Feature oder eine Funktion besonders fehleranfällig sein, während der Rest des Systems stabil ist.

# Welches Prinzip überrascht dich? Warum?
# TODO: Deine Antwort hier
# Defect Clustering überrascht mich, Fehler können ja überall auftreten, warum sollten sie sich clustern?
