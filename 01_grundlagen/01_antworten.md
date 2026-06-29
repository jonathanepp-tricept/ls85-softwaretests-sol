# Aufgaben Grundlagen

## Aufgabe 4

### Nennen Sie zwei konkrete Risiken, die durch das Weglassen von Tests entstehen

1. **(a)** Risiken ohne Tests:
   - Programmfehler bleiben unbemerkt und können zu finanziellen Schäden, Datenverlust oder Systemausfällen führen.
   - Die Benutzer verlieren Vertrauen in die Software, weil Fehler erst beim Kunden auffallen.

2. **(b)** Unterschied „Defekt“ und „Versagen“:
   - Ein Defekt ist ein Fehler im Quellcode, z.B. eine falsche Berechnungsformel für den Lagerbestand.
   - Ein Versagen tritt auf, wenn die Software im Alltag z.B. einen zu geringen Warenbestand anzeigt, was zu falschen Bestellungen führt.

3. **(c)** Frühzeitiges Testen ist wirtschaftlich sinnvoll, weil Fehler in frühen Phasen (z.B. Entwurf) viel günstiger behoben werden können als im Betrieb. Die „Rule of Ten“ besagt: Mit jeder späteren Entwicklungsphase steigen die Kosten für Fehlerbehebung um den Faktor 10.

## Aufgabe 5

**a)** Nur weil bis jetzt nichts passiert ist, heißt das nicht, dass nie etwas passieren wird. In der Vergangenheit ist es immer wieder vorgekommen, dass selbst bei hochkarätigen Projekten Fehler passiert sind, die zu enormen Schäden geführt haben. Ein Beispiel dafür ist der Absturz der Ariane-5-Rakete, der durch einen Ganzzahlüberlauf verursacht wurde. Das hat mehrere hundert Millionen Euro gekostet. Sollte es zu einem Versagen kommen, können hohe Kosten entstehen, entweder weil der Fehler behoben werden muss oder weil Kunden über das Versagen verärgert sind und Verträge kündigen.

**b)** **Möglicher Fehler (Error):** Ein Entwickler missversteht die Regel und nimmt an, Urlaubstage werden immer für eine 5-Tage-Woche berechnet, unabhängig vom Parameter arbeitstage_pro_woche.
**Möglicher Defekt (Defect):** Im Programmcode wird eine falsche Formel implementiert, sodass bei Teilzeitbeschäftigten zu viele oder zu wenige Urlaubstage berechnet werden.
**Mögliches Versagen (Failure):** Ein Mitarbeiter mit einer 3-Tage-Woche bekommt auf seinem Lohnzettel zu viele Urlaubstage ausgewiesen.

**Konsequenzen eines unentdeckten Defekts:** Wird ein Defekt im Lohnabrechnungssystem nicht entdeckt, kann dies zu falschen Urlaubsguthaben führen. Die Lohnabrechnung wäre fehlerhaft: Mitarbeiter würden zu viel oder zu wenig Urlaub nehmen oder darüber sogar rechtliche Auseinandersetzungen entstehen. Dies kann zu Unzufriedenheit, Vertrauensverlust oder gar finanziellen Schäden für das Unternehmen führen.

**c)** Das Grundprinzip 7 ist hier relevant, da ein System auch dann nicht „gut“ ist, wenn keine Fehler gefunden wurden – die Abwesenheit gefundener Fehler beweist keine Fehlerfreiheit und sagt nichts über die tatsächliche Nutzbarkeit oder Übereinstimmung mit den Anforderungen aus. Gerade in der Lohnabrechnung können auch Anforderungen, die nicht korrekt umgesetzt wurden, unentdeckt bleiben, wenn nur auf Fehlerfreiheit getestet wird. Deshalb sind zusätzliche Qualitätsmerkmale wie Funktionsumfang, Verständlichkeit und Benutzerfreundlichkeit ebenso zu prüfen.