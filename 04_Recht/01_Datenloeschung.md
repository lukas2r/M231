# Problematik Datenlöschung

## Warum ist «Löschen» nicht gleich «weg»?
- **Papierkorb / «Entfernen»**: Das Betriebssystem markiert nur den Speicherplatz als frei, entfernt also den Eintrag im Dateisystem. Die eigentlichen Daten bleiben auf der Disk, bis sie überschrieben werden. Mit Tools wie Recuva oder PhotoRec lassen sie sich oft wiederherstellen.
- **Schnellformatierung**: Es wird nur das Inhaltsverzeichnis neu angelegt, die Daten bleiben erhalten.
- **SSDs**: Wegen Wear-Leveling und Over-Provisioning schreibt der Controller Daten an andere Stellen als erwartet. Klassisches Überschreiben greift deshalb nicht zuverlässig. TRIM hilft, bietet aber keine Garantie.
- **Kopien überall**: Backups, Cloud-Synchronisation, E-Mail-Anhänge, Caches, Logfiles, Kopien bei Empfängern und Drittanbietern. Im Internet gilt: Was einmal veröffentlicht ist, wird kopiert, archiviert (z. B. Wayback Machine) und in Screenshots festgehalten. Das Internet vergisst nicht.

## Sicheres Löschen
| Datenträger | Methode |
|---|---|
| HDD | Mehrfach überschreiben (z. B. DBAN, `cipher /w:C:` unter Windows, `shred`). Heute genügt in der Regel ein Durchgang. |
| SSD | **ATA Secure Erase** bzw. NVMe Sanitize mit dem Herstellertool, oder: **von Anfang an verschlüsseln** (BitLocker) und dann den Schlüssel vernichten (Crypto-Erase) |
| Smartphone | Verschlüsselung aktiv lassen, dann auf Werkseinstellungen zurücksetzen |
| Defekte Datenträger / höchste Sicherheit | **Physische Zerstörung** (Schreddern, Degausser bei HDDs) durch einen zertifizierten Entsorger mit Vernichtungsprotokoll |

## Rechtliche Seite
- **Recht auf Löschung**: Nach Art. 32 DSG (bzw. Art. 17 DSGVO, «Recht auf Vergessenwerden») kann man die Löschung seiner Daten verlangen, wenn kein Rechtfertigungsgrund mehr besteht.
- **Speicherbegrenzung**: Personendaten müssen gelöscht oder anonymisiert werden, sobald sie für den Zweck nicht mehr nötig sind (Art. 6 Abs. 4 DSG).
- **Konflikt mit Aufbewahrungspflichten**: Geschäftsbücher und Belege müssen **10 Jahre** aufbewahrt werden (Art. 958f OR), Mehrwertsteuerdaten ebenfalls 10 Jahre, bei Immobilien 20 Jahre. Solche Daten dürfen also erst nach Ablauf der Frist gelöscht werden.
- **Konflikt mit Backups**: Gelöschte Daten können noch in Backups vorhanden sein. Ein Löschkonzept muss deshalb definieren, wie lange Backups aufbewahrt werden und ob Daten nach einer Wiederherstellung erneut gelöscht werden müssen.
- **Suchmaschinen**: Bei Google kann man die Entfernung von Suchergebnissen beantragen. Das Original auf der Website bleibt dabei aber bestehen.

## Fazit
Zuverlässig löschen kann man nur, wenn man weiss, **wo überall Kopien liegen**. Ein **Löschkonzept** mit Aufbewahrungsfristen, Verantwortlichkeiten und Löschmethoden sowie **Verschlüsselung von Anfang an** sind deshalb die wichtigsten Massnahmen. Privat gilt: Vor dem Posten nachdenken.
