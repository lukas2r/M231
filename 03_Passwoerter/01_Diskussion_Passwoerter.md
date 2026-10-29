# Diskussion Passwörter – MindMap

> ✏️ **TODO**: Diese Aufgabe ist ein **Austausch in der Gruppe**. Ergänze die MindMap mit den Punkten aus eurer Diskussion bzw. ersetze sie durch einen Screenshot eurer eigenen MindMap.

```mermaid
mindmap
  root((Passwörter))
    Gute Passwörter
      Länge vor Komplexität: mindestens 12–16 Zeichen
      Passphrase aus mehreren zufälligen Wörtern
      Für jeden Dienst ein eigenes Passwort
      Zufällig generiert
    Schlechte Passwörter
      123456, passwort, qwertz
      Name, Geburtsdatum, Haustier
      Wörter aus dem Wörterbuch
      Einfache Muster wie Sommer2026!
    Angriffe
      Brute Force
      Wörterbuchangriff
      Credential Stuffing nach Leaks
      Phishing
      Keylogger
      Rainbow Tables
    Aufbewahrung
      Passwortmanager
      Nicht auf einem Post-it
      Nicht unverschlüsselt im Browser oder in Dateien
    Zusätzlicher Schutz
      MFA / 2FA
      Passkeys
      Leaks prüfen mit haveibeenpwned
    Seitens Anbieter
      Hash mit Salt
      bcrypt / Argon2
      Rate Limiting und Sperre
```

## Wichtigste Erkenntnisse
- **Länge schlägt Komplexität.** Jedes zusätzliche Zeichen vervielfacht die Anzahl Kombinationen. Ein Beispiel: «Kaffee-Tram-Gletscher-Velo» ist sicherer und leichter zu merken als «K#7z!».
- **Wiederverwendung ist das grösste Risiko.** Nach einem Leak probieren Angreifer die Kombination aus E-Mail und Passwort automatisch bei anderen Diensten aus (Credential Stuffing).
- Häufige Zwangswechsel bringen wenig. Das NIST empfiehlt heute, Passwörter nur bei einem Verdacht auf Kompromittierung zu ändern.
- Die beste Lösung ist ein **Passwortmanager + MFA**, langfristig **Passkeys**.

## Meine Meinung / Diskussionspunkte aus der Gruppe
✏️ **TODO**
