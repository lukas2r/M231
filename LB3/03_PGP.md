# Verschlüsselung via PGP

## Was ist PGP?
**Pretty Good Privacy** (Phil Zimmermann, 1991) ist ein Verfahren zum **Verschlüsseln und Signieren** von E-Mails und Dateien. Der offene Standard heisst **OpenPGP** (RFC 4880 / RFC 9580), die freie Implementierung **GnuPG (GPG)**. PGP arbeitet **hybrid**: Die Nachricht wird mit einem zufälligen Sitzungsschlüssel (AES) verschlüsselt, dieser Schlüssel wiederum mit dem Public Key des Empfängers.

Vertrauensmodell: **Web of Trust**. Nutzer bestätigen sich gegenseitig die Echtheit ihrer Schlüssel (Key-Signing), statt einer zentralen Zertifizierungsstelle zu vertrauen. Zusätzlich vergleicht man den **Fingerprint** über einen zweiten Kanal.

## Durchführung
Werkzeug: ✏️ TODO (z. B. **Gpg4win/Kleopatra** unter Windows, **Thunderbird** mit integriertem OpenPGP oder Proton Mail)

### 1. Schlüsselpaar erzeugen
Kleopatra: *Datei → Neues OpenPGP-Schlüsselpaar*, Name und E-Mail angeben, mit Passphrase schützen.
Alternativ auf der Kommandozeile:
```bash
gpg --full-generate-key          # ECC (Ed25519/Curve25519) oder RSA 4096
gpg --list-keys --fingerprint
```
✏️ **TODO**: Screenshot und Fingerprint deines Schlüssels

### 2. Public Key exportieren und austauschen
```bash
gpg --armor --export deine@mail.ch > meinkey.asc
gpg --import kollege.asc
```
✏️ **TODO**: Mit wem hast du Schlüssel getauscht? Wie habt ihr den Fingerprint überprüft?

### 3. Nachricht verschlüsseln und signieren
```bash
gpg --armor --encrypt --sign -r kollege@mail.ch nachricht.txt   # → nachricht.txt.asc
```
### 4. Nachricht entschlüsseln und Signatur prüfen
```bash
gpg --decrypt nachricht.txt.asc
```
✏️ **TODO**: Screenshot einer erfolgreich entschlüsselten und verifizierten Nachricht

## Erkenntnisse
- Der **private Schlüssel** und seine Passphrase dürfen nie weitergegeben werden. Wer den privaten Schlüssel verliert, kann alte Nachrichten nicht mehr lesen. Erstelle deshalb ein Backup und ein **Widerrufszertifikat**.
- PGP verschlüsselt nur den **Inhalt**. **Betreff, Absender, Empfänger und Zeit** (die Metadaten) bleiben sichtbar.
- Beide Seiten müssen PGP einsetzen, das macht die Verbreitung schwierig. Messenger wie Signal oder Threema lösen das Problem benutzerfreundlicher.
