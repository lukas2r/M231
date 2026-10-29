# Backup-Konzept für mein Handy

> ✏️ **TODO**: Passe die Angaben an dein Gerät und deine Daten an. Danach **mit der Lehrperson besprechen** und den Termin und das Feedback unten eintragen.

## 1. Ausgangslage
| | |
|---|---|
| Gerät | ✏️ TODO (z. B. iPhone 15 / Samsung Galaxy S24) |
| Betriebssystem | ✏️ TODO (iOS / Android) |
| Speicherbelegung | ✏️ TODO GB von ✏️ TODO GB |

## 2. Was wird gesichert? (Datenbestand und Wichtigkeit)
| Daten | Wichtigkeit | Änderungshäufigkeit | Bemerkung |
|---|---|---|---|
| Fotos & Videos | sehr hoch (unersetzlich) | täglich | grösster Datenanteil |
| Kontakte | hoch | selten | |
| Chats (WhatsApp/Signal/Threema) | hoch | täglich | eigenes Backup der App nötig |
| 2FA-Authenticator | **kritisch** | selten | Ohne Backup droht der Ausschluss aus allen Konten |
| Notizen, Kalender | mittel | wöchentlich | meist schon über die Cloud synchronisiert |
| Schul- und Arbeitsdokumente | hoch | täglich | liegen in OneDrive (TBZ) |
| Apps & Einstellungen | niedrig | selten | lassen sich neu installieren |

## 3. Risiken (wogegen sichere ich mich ab?)
Verlust oder Diebstahl, Defekt (Wasser, Sturz), versehentliches Löschen, Malware, ein gesperrter Account, ein Fehler beim Update.

## 4. Backup-Strategie (nach 3-2-1)
| Kopie | Medium / Ort | Methode | Häufigkeit | Automatisch? |
|---|---|---|---|---|
| 1 – Original | Handy | – | – | – |
| 2 – Cloud (offsite, online) | iCloud bzw. Google One (oder verschlüsselt mit Proton Drive) | Geräte-Backup + Fotos-Synchronisation | täglich, beim Laden im WLAN | ✅ |
| 3 – Lokal (offline) | Externe SSD am PC | iOS: Backup über iTunes / Apple-Geräte-App (**verschlüsselt**). Android: Fotos/DCIM per USB kopieren oder Smart Switch. | monatlich | ❌ manuell (Kalendererinnerung) |
| Spezial: Chats | WhatsApp-Backup in iCloud/Google Drive mit **Ende-zu-Ende-Verschlüsselung** aktiviert | | täglich | ✅ |
| Spezial: 2FA | Authenticator mit verschlüsseltem Cloud-Backup + **Wiederherstellungscodes** im Passwortmanager | | bei jeder Änderung | – |

RPO: maximal 1 Tag Datenverlust bei Fotos und Chats.

## 5. Sicherheit des Backups
- Lokale Backups **verschlüsselt** (iOS: Option «Lokales Backup verschlüsseln»)
- Cloud-Konto mit starkem Passwort + **2FA**, iOS optional «Erweiterter Datenschutz» (E2E)
- Die externe SSD wird nach dem Backup getrennt und an einem anderen Ort gelagert.

## 6. Restore-Test
Alle 3 Monate: ein paar zufällige Fotos aus dem Backup öffnen und das Chat-Backup kontrollieren (Datum der letzten Sicherung). Einmal im Jahr bzw. beim Handywechsel: kompletter Restore auf ein Gerät.

## 7. Besprechung mit der Lehrperson
| Datum | Feedback |
|---|---|
| ✏️ TODO | ✏️ TODO |
