# Authentifizierung vs. Autorisierung

| | Authentifizierung (AuthN) | Autorisierung (AuthZ) |
|---|---|---|
| Frage | **Wer bist du?** | **Was darfst du?** |
| Zweck | Identität nachweisen bzw. überprüfen | Zugriffsrechte vergeben bzw. prüfen |
| Zeitpunkt | **zuerst** | **danach**, setzt AuthN voraus |
| Beispiele | Passwort, Fingerabdruck, Badge, OTP-Code | Dateirechte (NTFS), Rollen (Admin/User), Freigaben |
| Technik | Login, MFA, Kerberos, OpenID Connect | ACLs, RBAC, OAuth 2.0 (Scopes) |
| Fehler | «Falsches Passwort» (HTTP 401) | «Zugriff verweigert» (HTTP 403) |

Oft wird zwischen **Identifikation** (die Behauptung «Ich bin Lukas», z. B. der Benutzername) und **Authentifizierung** (der Beweis dafür, z. B. das Passwort) unterschieden.

## Alltagsbeispiele
- **Hotel**: An der Rezeption zeigst du deinen Ausweis (Authentifizierung). Die Zimmerkarte öffnet danach nur dein Zimmer und den Fitnessraum, nicht aber die anderen Zimmer (Autorisierung).
- **Flughafen**: Die Passkontrolle ist die Authentifizierung. Die Bordkarte erlaubt dir nur, ein bestimmtes Flugzeug zu betreten (Autorisierung).
- **Schulnetz TBZ**: Du meldest dich mit Benutzername und Passwort plus MFA an (Authentifizierung). Danach siehst du nur deine Kurse in Teams, als Lernende/r kannst du keine Noten ändern (Autorisierung).
- **Online-Banking**: Login mit Passwort und App (AuthN). Du siehst nur deine Konten, Zahlungen über einer Limite brauchen eine zusätzliche Freigabe (AuthZ).

## Authentifizierungsfaktoren
1. **Wissen**: Passwort, PIN, Sicherheitsfrage
2. **Besitz**: Smartphone (App, SMS), Hardware-Token (YubiKey), Smartcard
3. **Inhärenz / Sein**: Fingerabdruck, Gesichtserkennung, Iris, Stimme

Ergänzend gibt es Faktoren wie **Ort** oder **Verhalten**. Werden mehrere Faktoren kombiniert, spricht man von **MFA** (→ [MFA](11_MFA.md)).

## Prinzipien bei der Autorisierung
- **Least Privilege**: Jede Person bekommt nur die Rechte, die sie wirklich braucht.
- **Need to know**
- **Rollenbasiert (RBAC)**: Rechte werden an Rollen vergeben, nicht an Einzelpersonen.
