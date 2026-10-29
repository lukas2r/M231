# Symmetrische und asymmetrische Verschlüsselung

## Symmetrische Verschlüsselung
Für Ver- **und** Entschlüsselung wird **derselbe geheime Schlüssel** verwendet.

```
Alice ──[Klartext]──► 🔑 verschlüsseln ──[Geheimtext]──► 🔑 entschlüsseln ──[Klartext]──► Bob
              (gleicher Schlüssel auf beiden Seiten)
```
- **Beispiele**: AES (Standard, 128/256 Bit), ChaCha20, früher DES und 3DES; historisch Cäsar und Enigma
- ✅ Sehr **schnell**, eignet sich auch für grosse Datenmengen
- ❌ **Schlüsselaustauschproblem**: Wie bekommt Bob den Schlüssel sicher?
- ❌ **Schlüsselanzahl**: Bei *n* Teilnehmern braucht es n·(n−1)/2 Schlüssel, bei 100 Personen also 4950.

## Asymmetrische Verschlüsselung (Public-Key)
Jede Person hat ein **Schlüsselpaar**:
- **Öffentlicher Schlüssel (Public Key)**: Er darf an alle verteilt werden und dient zum **Verschlüsseln** bzw. zum Prüfen von Signaturen.
- **Privater Schlüssel (Private Key)**: Er bleibt geheim und dient zum **Entschlüsseln** bzw. zum Signieren.

```
Verschlüsseln:  Alice verschlüsselt mit Bobs PUBLIC Key → nur Bob kann mit seinem PRIVATE Key entschlüsseln
Signieren:      Alice signiert mit ihrem PRIVATE Key   → alle prüfen mit Alices PUBLIC Key
```
- **Beispiele**: RSA, Elliptische Kurven (ECC, z. B. Ed25519), Diffie-Hellman (Schlüsselaustausch)
- ✅ Kein geheimer Schlüsselaustausch nötig, jede Person braucht nur ein Schlüsselpaar
- ✅ Ermöglicht **digitale Signaturen**: Authentizität, Integrität und Nichtabstreitbarkeit
- ❌ Etwa 1000-mal **langsamer** als symmetrische Verfahren
- ❌ **Echtheit des Public Keys**: Gehört der Schlüssel wirklich Bob? Lösung: Zertifikate bzw. PKI oder das Web of Trust bei PGP.

## Hybride Verschlüsselung (Praxis)
In der Praxis werden beide Verfahren kombiniert, zum Beispiel bei **HTTPS/TLS, PGP und Signal**:
1. Ein zufälliger symmetrischer **Sitzungsschlüssel** wird erzeugt.
2. Dieser Schlüssel wird **asymmetrisch** mit dem Public Key des Empfängers verschlüsselt bzw. per Diffie-Hellman vereinbart.
3. Die eigentlichen Daten werden **symmetrisch** (AES) und damit schnell verschlüsselt.

So kombiniert man die Geschwindigkeit des symmetrischen Verfahrens mit dem einfachen Schlüsselaustausch des asymmetrischen.

## Vergleich
| | Symmetrisch | Asymmetrisch |
|---|---|---|
| Schlüssel | 1 gemeinsamer geheimer | Paar: öffentlich + privat |
| Geschwindigkeit | schnell | langsam |
| Schlüsselverteilung | Problem | einfach |
| Signaturen | nein | ja |
| Typische Schlüssellänge | 128–256 Bit (AES) | 2048–4096 Bit (RSA), 256 Bit (ECC) |
| Einsatz | Daten, Festplatten (BitLocker, VeraCrypt) | Schlüsselaustausch, Signaturen, E-Mail (PGP) |

## Abgrenzung zum Hashing
Hashing ist **keine** Verschlüsselung: Es gibt keinen Schlüssel und keinen Weg zurück (→ [Hash](02_Hash.md)).
