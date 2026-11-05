# Verschlüsselung via PGP

## Was ist PGP?
**Pretty Good Privacy** (Phil Zimmermann, 1991) ist ein Verfahren zum **Verschlüsseln und Signieren** von E-Mails und Dateien. Der offene Standard heisst **OpenPGP** (RFC 4880 / RFC 9580), die freie Implementierung **GnuPG (GPG)**. PGP arbeitet **hybrid**: Die Nachricht wird mit einem zufälligen Sitzungsschlüssel (AES) verschlüsselt, dieser Schlüssel wiederum mit dem Public Key des Empfängers.

Vertrauensmodell: **Web of Trust**. Nutzer bestätigen sich gegenseitig die Echtheit ihrer Schlüssel (Key-Signing), statt einer zentralen Zertifizierungsstelle zu vertrauen. Zusätzlich vergleicht man den **Fingerprint** über einen zweiten Kanal.

## Durchführung
Werkzeug: **GnuPG 2.4** (Kommandozeile). Unter Windows bekommt man dasselbe mit **Gpg4win/Kleopatra** (gratis, Open Source, gpg4win.org) über eine grafische Oberfläche.

Durchgeführt als **Test mit zwei Schlüsselpaaren**: «Lukas» und «Testpartner». Jedes Paar liegt in einem eigenen Schlüsselbund, so als wären es zwei verschiedene Personen. Die E-Mail-Adressen sind Testadressen.

### 1. Schlüsselpaar erzeugen
Hauptschlüssel **Ed25519** zum Signieren, dazu ein Unterschlüssel **Curve25519 (cv25519)** zum Verschlüsseln, 1 Jahr gültig.
```bash
gpg --quick-generate-key "Lukas (M231 Test) <lukas@m231.test>" ed25519 sign 1y
gpg --quick-add-key <Fingerprint> cv25519 encr 1y
gpg --list-keys --fingerprint
```
Ergebnis:
```
pub   ed25519 2026-11-05 [SC] [expires: 2027-11-05]
      9155 5150 110C F158 0ADF  465C E989 1B10 DC65 827F
uid           [ultimate] Lukas (M231 Test) <lukas@m231.test>
sub   cv25519 2026-11-05 [E] [expires: 2027-11-05]
```
`[SC]` = Signieren und Zertifizieren, `[E]` = Verschlüsseln (Encrypt).

### 2. Public Keys austauschen
Beide exportieren ihren **öffentlichen** Schlüssel und importieren den des anderen. Der private Schlüssel verlässt den eigenen Schlüsselbund nie.
```bash
gpg --armor --export lukas@m231.test > lukas.pub      # an Partner geben
gpg --import partner.pub                              # Schlüssel des Partners importieren
```
**Fingerprint prüfen:** Im Echtbetrieb vergleicht man den Fingerprint über einen zweiten Kanal, zum Beispiel persönlich oder am Telefon. So stellt man sicher, dass der Schlüssel wirklich der Person gehört und nicht von einem Angreifer untergeschoben wurde (Man-in-the-Middle).

### 3. Nachricht verschlüsseln und signieren (Partner → Lukas)
Der Partner verschlüsselt mit **Lukas' öffentlichem Schlüssel** und signiert mit **seinem privaten Schlüssel**:
```bash
gpg --armor --encrypt --sign -r lukas@m231.test nachricht.txt
```
Klartext: `Hallo Lukas, Treffpunkt morgen 8 Uhr vor dem Schulzimmer. Gruss, Partner`

Geheimtext (`nachricht.txt.asc`), ohne den privaten Schlüssel nicht lesbar:
```
-----BEGIN PGP MESSAGE-----

hF4DWESb9MUGmpcSAQdA9vhaAns4WRby7PVwWI6XAkPpI2CEyopPR1zrdLWrkiww
a+6aKvAu/15jXA0bUlx8edZsbIdCH9VJbW0USpdVqQInGyGi9PwMcwVxRUr0AuqH
1MBYAQkCEP+nJzjv7MuEutH2uDymC2G4D6ytVN1NSFhzPmQR0VihLMbrC1R9qObu
HwYZzW0EQ3NQxVa+lReL/DdVoLzah6/9DtO6wMPdoJBM9igf/GO/VhkBioLCfQKo
w1Qv0exZGCwjMY2qeShtqvr5y/wHoshVd7lENekASJ62f9XOhFzxstf5FarMlR4l
I8QnEwCBMib6ZHjmNeBFLLX9T1OynIhzXs9oQZIW5EsUAZjDPNgZeYVUQVGswhYE
3LEPEx08zFIN/Zf2x/qW5XrPQvrJ3ke7r/QW29TSv7o14ntJwrdc99Ndm/BrRW7X
QP8QrMwVaVBRK42y1i2PRzI7BwGsVn8Zg/Apiip0mW/CE3tjyvZnGGiVfA==
=VuPZ
-----END PGP MESSAGE-----
```

### 4. Entschlüsseln und Signatur prüfen (bei Lukas)
```bash
gpg --decrypt nachricht.txt.asc
```
```
gpg: encrypted with cv25519 key, ID 58449BF4C5069A97, created 2026-11-05
      "Lukas (M231 Test) <lukas@m231.test>"
Hallo Lukas, Treffpunkt morgen 8 Uhr vor dem Schulzimmer. Gruss, Partner
gpg: Signature made Thu Nov  5 13:12:40 2026 CET
gpg: Good signature from "Testpartner (M231 Test) <partner@m231.test>" [unknown]
gpg: WARNING: Using untrusted key!
```
- ✅ **Entschlüsselt**: Die Nachricht ist wieder lesbar, also ist die **Vertraulichkeit** erfüllt.
- ✅ **«Good signature»**: Die Nachricht stammt vom Partner und wurde unterwegs nicht verändert. Damit sind **Authentizität und Integrität** erfüllt.
- ⚠️ **«untrusted key»**: GnuPG weist darauf hin, dass niemand bestätigt hat, dass der Schlüssel wirklich dem Partner gehört. Das ist genau der Grund für den Fingerprint-Vergleich bzw. das **Web of Trust**. Nach der Prüfung signiert man den Schlüssel (`gpg --sign-key partner@m231.test`), dann verschwindet die Warnung.

### 5. Gegenprobe: Ohne privaten Schlüssel geht nichts
Selbst der **Absender** kann seine eigene verschlüsselte Nachricht nicht mehr öffnen, weil sie nur für Lukas' Schlüssel verschlüsselt ist:
```
gpg: public key decryption failed: No secret key
gpg: decryption failed: No secret key
```

## Erkenntnisse
- Der **private Schlüssel** und seine Passphrase dürfen nie weitergegeben werden. Wer den privaten Schlüssel verliert, kann alte Nachrichten nicht mehr lesen. Erstelle deshalb ein Backup und ein **Widerrufszertifikat**.
- PGP verschlüsselt nur den **Inhalt**. **Betreff, Absender, Empfänger und Zeit** (die Metadaten) bleiben sichtbar.
- Beide Seiten müssen PGP einsetzen, das macht die Verbreitung schwierig. Messenger wie Signal oder Threema lösen das Problem benutzerfreundlicher.
