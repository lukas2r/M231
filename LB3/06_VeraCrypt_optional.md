# VeraCrypt *(optional)*

## Was ist VeraCrypt?
VeraCrypt ist eine kostenlose Open-Source-Software (Nachfolger von TrueCrypt) für die **On-the-fly-Verschlüsselung**. Damit lässt sich
- ein **verschlüsselter Container** erstellen: eine Datei, die als virtuelles Laufwerk eingebunden wird,
- eine ganze Partition oder ein USB-Stick verschlüsseln,
- die Systempartition verschlüsseln (mit Pre-Boot-Authentifizierung).

Algorithmen: AES, Serpent, Twofish sowie Kaskaden davon. Für die Schlüsselableitung aus dem Passwort wird PBKDF2 mit vielen Iterationen verwendet. Eine Besonderheit sind **Hidden Volumes**, versteckte Volumes innerhalb eines Containers für «glaubhafte Abstreitbarkeit».

## Anleitung: Container erstellen
1. VeraCrypt von veracrypt.fr installieren
2. *Volume erstellen* → «Verschlüsselte Containerdatei erstellen» → *Standard-VeraCrypt-Volume*
3. Speicherort und Dateiname wählen, z. B. `Dokumente\tresor.hc`
4. Verschlüsselung: AES, Hash: SHA-512
5. Grösse festlegen, z. B. 500 MB
6. Ein **starkes Passwort** wählen (lange Passphrase, im Passwortmanager speichern)
7. Maus zufällig bewegen (Entropie sammeln) → *Formatieren*
8. Im Hauptfenster einen Laufwerksbuchstaben wählen → *Datei…* → Container auswählen → *Einbinden* → Passwort eingeben
9. Dateien wie auf einem normalen Laufwerk ablegen → am Schluss **Trennen**

✏️ **TODO**: Screenshots von Schritt 2, 8 und dem eingebundenen Laufwerk im Explorer

## Vergleich mit Cryptomator
| | VeraCrypt | Cryptomator |
|---|---|---|
| Prinzip | ein grosser Container bzw. eine Partition | jede Datei wird einzeln verschlüsselt |
| Ideal für | lokale Laufwerke, USB-Sticks, System | **Cloud-Speicher** (OneDrive, Dropbox), da nur geänderte Dateien synchronisiert werden |
| Systemverschlüsselung | ja | nein |
| Hidden Volume | ja | nein |
| Mobile Apps | nein (nur Drittanbieter) | ja (iOS/Android) |

## Bedeutung für den Berufsalltag
Sensible Daten wie Kundendaten, Passwörter oder Lohnlisten auf USB-Sticks oder in der Cloud sollten **immer verschlüsselt** sein. Geht ein Datenträger verloren, sind die Daten so nicht kompromittiert. Das ist eine Massnahme der Datensicherheit nach Art. 8 DSG.
