# Überprüfung des Backups

> ✏️ **TODO**: Bei dieser Aufgabe zeigst du der Lehrperson an einem Termin, dass dein Backup funktioniert. Führe die Checks durch und trage die Resultate ein.

## Warum überprüfen?
«Ein Backup, dessen Wiederherstellung nie getestet wurde, ist kein Backup.» Typische Probleme, die erst beim Restore auffallen:
- Das Backup läuft seit Wochen nicht mehr (die Disk war nicht angeschlossen, das Abo ist abgelaufen, der Speicher ist voll).
- Wichtige Ordner waren gar nicht ausgewählt.
- Das Backup ist beschädigt oder unvollständig.
- Passwort oder Schlüssel für das verschlüsselte Backup sind unbekannt.
- Der Restore dauert viel länger als erwartet (RTO).

## Prüfprotokoll
| Prüfpunkt | Handy | PC | Ergebnis / Bemerkung |
|---|---|---|---|
| Datum der letzten erfolgreichen Sicherung | ✏️ | ✏️ | |
| Läuft das Backup automatisch? | ✏️ | ✏️ | |
| Sind alle wichtigen Daten enthalten? (Abgleich mit dem Konzept) | ✏️ | ✏️ | |
| Ist das Backup verschlüsselt? | ✏️ | ✏️ | |
| Ist eine Kopie offline bzw. offsite? (3-2-1) | ✏️ | ✏️ | |
| **Restore-Test**: Eine Datei löschen und aus dem Backup wiederherstellen | ✏️ | ✏️ | |
| Ist die wiederhergestellte Datei identisch? (z. B. Hash-Vergleich mit `Get-FileHash`) | ✏️ | ✏️ | |
| Dauer des Restores | ✏️ | ✏️ | |

### Beispiel Hash-Vergleich (PowerShell)
```powershell
Get-FileHash "C:\Users\<name>\Documents\test.docx" -Algorithm SHA256
Get-FileHash "D:\Restore\test.docx" -Algorithm SHA256
# Gleiche Hashwerte bedeuten: Die Datei ist unverändert wiederhergestellt (Integrität ✅)
```

## Termin mit der Lehrperson
| Datum | Gezeigt | Feedback |
|---|---|---|
| ✏️ TODO | | |

## Massnahmen aus der Überprüfung
✏️ **TODO**: Was hast du nach der Prüfung angepasst?
