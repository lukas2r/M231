# Sicheres Cloud-Backup

## Vorteile
- **Offsite**: Schutz vor Brand, Wasser und Diebstahl zu Hause
- **Automatisch** und ohne Zutun, dadurch kaum vergessene Backups
- Von überall und von jedem Gerät aus zugänglich
- **Versionierung** und Papierkorb (Wiederherstellung älterer Stände, teilweise ein Schutz vor Ransomware)
- Skalierbar, kein Hardware-Unterhalt
- Professionelle Rechenzentren mit eigener Redundanz

## Nachteile
- **Datenschutz**: Die Daten liegen bei einem Dritten, oft in den USA (US CLOUD Act). Der Anbieter kann die Daten bei Server-seitiger Verschlüsselung grundsätzlich lesen.
- **Abhängigkeit** vom Anbieter: Kündigung, Konkurs, Preisänderungen, gesperrter Account
- **Internet nötig**: Upload und Restore grosser Datenmengen dauern lange.
- Laufende **Kosten**
- Konto-Hacking: Wer Zugangsdaten stiehlt, hat Zugriff auf alle Daten, deshalb ist MFA Pflicht.
- **Synchronisation ≠ Backup**: Bei reinem Sync (OneDrive, Dropbox) werden Löschungen und von Ransomware verschlüsselte Dateien mitsynchronisiert.

## Verschlüsselung
| Art | Wer hat den Schlüssel? | Bedeutung |
|---|---|---|
| **Transportverschlüsselung** (TLS/HTTPS) | – | Schützt nur unterwegs |
| **Server-seitige Verschlüsselung** (at rest) | **Anbieter** | Schützt vor Diebstahl der Disks im Rechenzentrum, aber nicht vor dem Anbieter oder vor Behörden. Standard bei OneDrive, Google Drive, Dropbox. |
| **Client-seitige / Ende-zu-Ende-Verschlüsselung (Zero-Knowledge)** | **Nur ich** | Die Daten werden vor dem Upload auf meinem Gerät verschlüsselt. Der Anbieter sieht nur Datensalat. ⚠️ Wer den Schlüssel bzw. das Passwort verliert, verliert die Daten. |

**Anbieter mit E2E**: Proton Drive (CH), Tresorit (CH/HU), Filen, pCloud Crypto, Apple iCloud mit «Erweitertem Datenschutz», Backblaze mit privatem Schlüssel.
**Selbst verschlüsseln**: Mit **Cryptomator** oder VeraCrypt vor dem Upload zu OneDrive oder Google Drive (→ [VeraCrypt](../02_Verschluesselung/05_VeraCrypt.md)), oder mit Backup-Tools mit eigener Verschlüsselung wie Duplicati, restic oder Kopia.

## Empfehlungen für ein sicheres Cloud-Backup
1. Einen Anbieter mit **Zero-Knowledge-E2E** wählen oder clientseitig selbst verschlüsseln
2. Für sensible Daten möglichst einen **Serverstandort in der Schweiz bzw. EU**
3. **Starkes Passwort + MFA** für das Cloud-Konto
4. **Versionierung** aktivieren, möglichst lange Aufbewahrung
5. Echte Backup-Software statt reiner Synchronisation
6. Den Schlüssel bzw. das Passwort sicher aufbewahren (Passwortmanager und Notfallblatt)
7. Cloud-Backup **zusätzlich** zu einem lokalen Offline-Backup nach der 3-2-1-Regel
8. Restore regelmässig testen

## Praxis
✏️ **TODO**: Richte zum Beispiel Cryptomator mit deinem OneDrive ein, lege eine Datei in den Tresor und kontrolliere im OneDrive-Webportal, dass dort nur verschlüsselte Dateinamen und Inhalte sichtbar sind. Füge einen Screenshot ein.
