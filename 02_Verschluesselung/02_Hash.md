# Hash-Funktionen

## Was ist eine Hash-Funktion?
Eine Hash-Funktion berechnet aus einer **beliebig langen Eingabe** einen **Wert mit fester Länge** (Hash, Prüfsumme, «digitaler Fingerabdruck»).

Eigenschaften einer kryptografischen Hash-Funktion:
| Eigenschaft | Bedeutung |
|---|---|
| Deterministisch | Gleiche Eingabe ergibt immer denselben Hash. |
| Einwegfunktion | Aus dem Hash lässt sich die Eingabe nicht zurückrechnen. Das ist **keine** Verschlüsselung. |
| Lawineneffekt | Schon eine minimale Änderung ergibt einen komplett anderen Hash. |
| Kollisionsresistenz | Es ist praktisch unmöglich, zwei verschiedene Eingaben mit gleichem Hash zu finden. |
| Feste Länge | MD5 = 128 Bit, SHA-1 = 160 Bit, SHA-256 = 256 Bit |

## Eigene Berechnungen
Berechnet mit Python (`hashlib`). Unter Windows geht es auch so: `Get-FileHash datei.txt -Algorithm SHA256` (PowerShell) bzw. `certutil -hashfile datei.txt SHA256`.

| Eingabe | MD5 | SHA-256 |
|---|---|---|
| `Hallo` | d1bf93299de1b68e6d382c893bf1215f | 753692ec36adb4c794c973945eb2a99c1649703ea6f76bf259abb4fb838e013e |
| `hallo` | 598d4c200461b81522a3328565c25f7c | d3751d33f9cd5049c4af2b462735457e4d3baf130bcbb87f389e349fbaeb20b9 |
| `Hallo!` | 1c8a4b25c96f385671a0989bd50daf8f | 357a57fe73d6c63bb1923e970f79a924db3a3609eb9797547784a94ee38fc3df |
| `Das ist ein Test` | b112c76d02b5832e8d83b74c102e0ca5 | c423b0dcb3697b21d846dbf01f6f2438fbc973078bd8fc671551f5b98e8af0f0 |

➡️ Schon ein anderer Grossbuchstabe oder ein einziges Ausrufezeichen ändert den gesamten Hash. Das ist der **Lawineneffekt**.

## Hash-Kollisionen
Eine **Kollision** liegt vor, wenn zwei *verschiedene* Eingaben denselben Hash ergeben. Weil unendlich viele Eingaben auf endlich viele Hashwerte abgebildet werden, muss es Kollisionen geben (**Schubfachprinzip**). Bei einer guten Hash-Funktion darf man sie aber praktisch nicht *finden* können.

- **Geburtstagsparadoxon**: Für eine Kollision braucht man nicht 2ⁿ, sondern nur etwa 2ⁿ/² Versuche. Bei MD5 (128 Bit) sind das ca. 2⁶⁴.
- **MD5** gilt als **gebrochen**: Seit 2004 lassen sich Kollisionen in Sekunden erzeugen. Bekannt sind zum Beispiel zwei verschiedene Bilder oder PDFs mit identischem MD5-Hash. Die Malware Flame nutzte 2012 eine MD5-Kollision, um ein Microsoft-Zertifikat zu fälschen.
- **SHA-1** ist ebenfalls **gebrochen**: Google und CWI präsentierten 2017 mit «SHAttered» zwei verschiedene PDFs mit gleichem SHA-1-Hash.
- **SHA-256 / SHA-3** gelten heute als sicher.

✏️ **TODO**: Lade die beiden Beispiel-Dateien aus dem Auftrag (bzw. von shattered.io) herunter, berechne die Hashes mit `Get-FileHash -Algorithm SHA1` und `-Algorithm SHA256` und trage die Resultate hier ein.

## Anwendungen
- **Passwortspeicherung**: Gespeichert wird nur der Hash, mit **Salt** und einem langsamen Verfahren wie bcrypt, scrypt oder Argon2. Der Salt verhindert Angriffe mit Rainbow Tables.
- **Integritätsprüfung** von Downloads (Vergleich mit dem veröffentlichten SHA-256-Wert)
- **Digitale Signaturen**: Signiert wird der Hash eines Dokuments.
- **Git**: Jeder Commit wird über einen Hash identifiziert (SHA-1, Umstellung auf SHA-256 möglich).
- **Blockchain**
