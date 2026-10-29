# Passwortmanager evaluieren, installieren und nutzen

## Was ist ein Passwortmanager?
Ein Passwortmanager speichert alle Zugangsdaten in einem **verschlüsselten Tresor**, der mit **einem Master-Passwort** (und idealerweise MFA) geschützt ist. Er generiert zufällige, starke Passwörter und füllt sie automatisch aus. Weil das Autofill nur auf der richtigen Domain funktioniert, bietet er zusätzlich Schutz vor Phishing.

## Evaluation
| Kriterium | Bitwarden | KeePassXC | 1Password | Proton Pass | Browser (Chrome/Edge) |
|---|---|---|---|---|---|
| Kosten | Gratis (Premium ca. 10 $/Jahr) | Gratis | ca. 36 $/Jahr | Gratis / Plus | Gratis |
| Open Source | ✅ | ✅ | ❌ | ✅ | teilweise |
| Speicherort | Cloud (oder selbst gehostet) | **lokale Datei** (.kdbx) | Cloud | Cloud (CH) | Cloud des Browser-Anbieters |
| Zero-Knowledge / E2E | ✅ | ✅ (lokal) | ✅ | ✅ | eingeschränkt |
| Sync über Geräte | ✅ automatisch | manuell (z. B. via Cloud-Ordner) | ✅ | ✅ | ✅ |
| Apps (Windows, macOS, iOS, Android) | ✅ | Desktop; Mobile über KeePassDX/Strongbox | ✅ | ✅ | ✅ |
| Unabhängige Audits | ✅ | ✅ | ✅ | ✅ | – |
| Passkeys | ✅ | ✅ | ✅ | ✅ | ✅ |
| Teilen / Familie | ✅ | ❌ | ✅ | ✅ | eingeschränkt |

### Entscheid
**Meine Wahl:** ✏️ TODO (Vorschlag: **Bitwarden**)
**Begründung (Vorschlag):** Bitwarden ist gratis, Open Source und regelmässig auditiert. Die Ende-zu-Ende-Verschlüsselung funktioniert nach dem Zero-Knowledge-Prinzip, und der Tresor synchronisiert sich automatisch zwischen PC und Handy. Wer die Daten nicht in der Cloud haben möchte, wählt **KeePassXC**: Dort bleibt die Datenbank vollständig lokal.

## Installation und Einrichtung
1. Konto auf bitwarden.com erstellen
2. Ein **starkes Master-Passwort** wählen (Passphrase mit mindestens 4–5 Wörtern). Es ist das einzige Passwort, das man sich noch merken muss, und es kann **nicht wiederhergestellt** werden.
3. **2FA** für den Tresor aktivieren (Authenticator-App) und den Wiederherstellungscode notieren
4. Browser-Erweiterung und Handy-App installieren
5. Passwörter aus dem Browser importieren, danach **im Browser löschen** und das Speichern im Browser deaktivieren
6. Mit dem Generator schwache oder doppelte Passwörter ersetzen (Bericht «Wiederverwendete Passwörter»)

✏️ **TODO**: Screenshots von Installation, Tresor (Passwörter unkenntlich machen!) und Generator

## Risiken
- Single Point of Failure: Das Master-Passwort und der 2FA-Wiederherstellungscode müssen sicher aufbewahrt werden.
- Auch Anbieter können angegriffen werden (z. B. der LastPass-Breach 2022). Dank Zero-Knowledge schützt dann das starke Master-Passwort den gestohlenen Tresor.
- Malware auf dem Gerät kann den entsperrten Tresor auslesen. Deshalb ist eine automatische Sperre nach Inaktivität wichtig.
