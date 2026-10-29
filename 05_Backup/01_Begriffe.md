# Backup – Fachbegriffe

| Begriff | Erklärung |
|---|---|
| **Backup (Datensicherung)** | Eine Kopie von Daten, mit der man den Originalzustand nach einem Verlust wiederherstellen kann |
| **Restore** | Die Wiederherstellung von Daten aus einem Backup |
| **Archivierung** | Langfristige, unveränderbare Aufbewahrung von Daten, die nicht mehr aktiv gebraucht werden (z. B. wegen gesetzlicher Fristen). Die Originale werden danach oft gelöscht. Ein Backup ist hingegen eine Kopie aktiver Daten. |
| **Vollbackup (Full)** | Alle ausgewählten Daten werden gesichert. ✅ einfacher Restore ❌ viel Platz und Zeit |
| **Inkrementelles Backup** | Nur die Änderungen **seit dem letzten Backup** jeglicher Art. ✅ schnell und klein ❌ Für einen Restore braucht es das Vollbackup **und alle** Inkremente. |
| **Differenzielles Backup** | Alle Änderungen **seit dem letzten Vollbackup**. ✅ Für einen Restore braucht es nur Vollbackup + letztes Differenzial ❌ wird mit der Zeit grösser |
| **Image / Systemabbild** | Eine bitgenaue Kopie einer ganzen Partition bzw. Disk inklusive Betriebssystem, Programmen und Einstellungen |
| **Spiegelung (Mirror) / Synchronisation** | Quelle und Ziel werden identisch gehalten. ⚠️ **Kein echtes Backup**: Gelöschte oder verschlüsselte Dateien (Ransomware) werden mitgespiegelt. |
| **RAID** | Redundante Festplatten (z. B. RAID 1 oder RAID 5). Schützt vor dem Ausfall einer Disk, aber **nicht** vor Löschen, Ransomware oder Brand. **RAID ist kein Backup.** |
| **Versionierung** | Mehrere ältere Stände einer Datei bleiben erhalten. |
| **Generationenprinzip** (Grossvater-Vater-Sohn) | Rotation der Sicherungen: täglich (Sohn), wöchentlich (Vater), monatlich (Grossvater) |
| **Aufbewahrungsdauer (Retention)** | Wie lange Backups behalten werden |
| **3-2-1-Regel** | **3** Kopien der Daten, auf **2** verschiedenen Medientypen, davon **1** ausser Haus (offsite). Erweitert zu 3-2-1-1-0: 1 Kopie offline bzw. unveränderbar, 0 Fehler bei der Prüfung. |
| **Offline-Backup** | Der Datenträger ist nach der Sicherung vom System getrennt (externe Disk, Band). Er ist deshalb vor Ransomware geschützt. |
| **Online-Backup** | Das Backup-Ziel ist ständig verbunden bzw. erreichbar (NAS, Cloud). Das ist bequem und automatisiert, aber angreifbar. |
| **Offsite / Onsite** | Das Backup liegt ausserhalb bzw. innerhalb des eigenen Standorts. |
| **Cloud-Backup** | Sicherung bei einem Online-Anbieter (→ [Cloud-Backup](04_Cloud_Backup.md)) |
| **Immutable Backup** | Ein unveränderbares Backup, das eine bestimmte Zeit lang nicht gelöscht werden kann (WORM, Object Lock) |
| **RPO** (Recovery Point Objective) | Wie viel Datenverlust (Zeit) maximal tolerierbar ist. Ein RPO von 24 h bedeutet ein tägliches Backup. |
| **RTO** (Recovery Time Objective) | Wie schnell das System wieder laufen muss |
| **Backup-Konzept** | Dokumentiert, *was*, *wann*, *wie*, *wohin*, *wie lange* und *von wem* gesichert wird und wie der Restore getestet wird |
| **Restore-Test** | Das regelmässige Prüfen, ob sich Daten tatsächlich wiederherstellen lassen. Ein ungetestetes Backup ist kein Backup. |
