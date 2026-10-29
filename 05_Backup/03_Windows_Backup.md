# Windows Backup einrichten

## Möglichkeiten in Windows 11
| Tool | Was wird gesichert? | Ziel | Typ |
|---|---|---|---|
| **Windows-Sicherung** (App «Windows Backup») | Ordner (Desktop, Dokumente, Bilder…), App-Liste, Einstellungen, Anmeldedaten | **OneDrive / Microsoft-Konto** | Online |
| **Dateiversionsverlauf** (File History) | Versionen der Dateien in Benutzerordnern | **Externe Disk** / Netzlaufwerk | Offline (wenn nach dem Backup getrennt) |
| **Sichern und Wiederherstellen (Windows 7)** | **Systemabbild** (Image) + Dateien | Externe Disk / Netzlaufwerk | Offline |

## Durchführung
### A) Online-Backup mit «Windows-Sicherung» bzw. OneDrive
1. *Einstellungen → Konten → Windows-Sicherung*
2. «OneDrive-Ordnersynchronisierung» → Desktop, Dokumente und Bilder aktivieren
3. «Meine Apps merken» und «Meine Einstellungen merken» aktivieren
✏️ **TODO**: Screenshot

### B) Offline-Backup mit dem Dateiversionsverlauf
1. Externe Disk anschliessen
2. *Systemsteuerung → System und Sicherheit → Dateiversionsverlauf* → «Einschalten»
3. *Erweiterte Einstellungen*: Intervall (z. B. stündlich) und Aufbewahrung (z. B. 1 Jahr) festlegen
4. «Jetzt ausführen» → nach dem Backup die Disk **trennen**
5. Restore-Test: «Persönliche Dateien wiederherstellen» → eine ältere Version einer Datei zurückholen
✏️ **TODO**: Screenshots von Schritt 2 und vom erfolgreichen Restore

### C) Systemabbild
*Systemsteuerung → Sichern und Wiederherstellen (Windows 7) → Systemabbild erstellen* → externe Disk wählen. Zusätzlich einen **Wiederherstellungsdatenträger** erstellen (USB-Stick, über die Suche «Wiederherstellungslaufwerk»).
✏️ **TODO**: Screenshot

> Hinweis: Auf einem verwalteten Schul-PC (Win11 Education) sind einzelne Optionen eventuell durch die IT gesperrt. In diesem Fall die Aufgabe auf einem privaten Gerät oder in einer VM durchführen.

## Unterschied Offline- vs. Online-Backup
| | Offline-Backup | Online-Backup |
|---|---|---|
| Definition | Das Backup-Medium ist nach der Sicherung **physisch bzw. logisch getrennt**. | Das Backup-Ziel ist **ständig verbunden** (Cloud, NAS). |
| Beispiele | Externe Disk, die danach abgezogen wird; Band; USB-Stick | OneDrive, iCloud, Backblaze, ständig gemountetes NAS |
| Schutz vor Ransomware / Hacker | ✅ hoch (nicht erreichbar) | ⚠️ gefährdet, ausser bei Versionierung oder immutable Backups |
| Schutz vor Brand, Diebstahl am Standort | ❌ wenn am selben Ort gelagert | ✅ offsite |
| Automatisierung | ❌ manuell, man muss daran denken | ✅ läuft automatisch |
| Restore-Geschwindigkeit | ✅ schnell (USB) | ❌ abhängig von der Internetverbindung |
| Kosten | einmalig (Disk) | laufend (Abo) |
| Datenschutz | ✅ volle Kontrolle | ⚠️ Daten liegen beim Anbieter, eventuell im Ausland |

**Fazit:** Die beiden Varianten ergänzen sich. Nach der 3-2-1-Regel nutzt man **beide**: das Online-Backup für Komfort und Offsite-Schutz, das Offline-Backup gegen Ransomware.
