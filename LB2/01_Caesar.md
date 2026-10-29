# Cäsar-Chiffre

## Funktionsweise
Die Cäsar-Chiffre ist eine **symmetrische Substitutionschiffre**. Jeder Buchstabe wird um eine feste Anzahl Stellen *k* (den Schlüssel) im Alphabet verschoben.

- Verschlüsseln: `C = (P + k) mod 26`
- Entschlüsseln: `P = (C − k) mod 26`

Beispiel mit k = 3:
```
Klar:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Geheim:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

## Eigene Beispiele
| Klartext | Schlüssel | Geheimtext |
|---|---|---|
| Datenschutz ist wichtig | 3 | Gdwhqvfkxwc lvw zlfkwlj |
| Treffpunkt morgen um acht in der Mensa | 7 | Aylmmwbura tvynlu bt hjoa pu kly Tluzh |

Die Beispiele wurden mit dem Skript [`caesar.py`](caesar.py) erstellt und überprüft.

## Austausch in der Klasse
| Von | Erhaltener Geheimtext | Schlüssel | Entschlüsselt |
|---|---|---|---|
| ✏️ TODO | | | |
| ✏️ TODO | | | |

## Wie sicher ist die Cäsar-Chiffre?
**Gar nicht sicher.**
1. **Brute Force**: Es gibt nur 25 sinnvolle Schlüssel. Alle kann man in Sekunden durchprobieren (`python caesar.py brute "..."`).
2. **Häufigkeitsanalyse**: Im Deutschen ist «E» mit etwa 17 % der häufigste Buchstabe. Der häufigste Buchstabe im Geheimtext verrät deshalb meist direkt den Schlüssel.
3. Gleiche Klartextbuchstaben ergeben immer gleiche Geheimtextbuchstaben, die Muster bleiben also erhalten.

Ausserdem gibt es das **Schlüsselaustauschproblem**: Beide Seiten müssen den Schlüssel vorher kennen. Er muss deshalb über einen sicheren Kanal ausgetauscht werden. Dieses Problem besteht bei allen symmetrischen Verfahren (→ siehe [Symmetrisch/Asymmetrisch](12_Symmetrisch_Asymmetrisch.md)).

Verbesserungen in der Geschichte: die Vigenère-Chiffre (Schlüsselwort statt fester Verschiebung), die Enigma und heute AES.
