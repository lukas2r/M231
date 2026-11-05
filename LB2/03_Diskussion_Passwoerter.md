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

## Meine Meinung
Früher habe ich für viele Dienste ähnliche Passwörter verwendet. Nach dieser Diskussion ist mir klar, dass gerade das gefährlich ist, weil ein einziges Leak dann mehrere Konten öffnet. Für mich ist die beste Lösung ein Passwortmanager mit einem langen Master-Passwort (Passphrase) plus MFA überall dort, wo es angeboten wird. Langfristig finde ich Passkeys am besten, weil man sich nichts merken muss und Phishing nicht mehr funktioniert.

## Diskussionspunkte aus der Gruppe
✏️ **TODO**: Punkte, die in eurer Gruppe gefallen sind
