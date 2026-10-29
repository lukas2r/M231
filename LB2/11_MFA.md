# Multi-Faktor-Authentifizierung (MFA)

## Definition
Bei **MFA** müssen sich Benutzer mit **mindestens zwei Faktoren aus verschiedenen Kategorien** authentifizieren:

| Kategorie | Beispiele |
|---|---|
| Wissen | Passwort, PIN |
| Besitz | Smartphone mit Authenticator-App, SMS, Hardware-Key (YubiKey), Smartcard, Bankkarte |
| Inhärenz (Biometrie) | Fingerabdruck, Face ID, Iris |

⚠️ Zwei Faktoren aus **derselben** Kategorie, zum Beispiel Passwort und Sicherheitsfrage, sind **keine** echte MFA.

## 2FA
**Zwei-Faktor-Authentifizierung** ist der häufigste Spezialfall von MFA, meist mit Wissen und Besitz kombiniert.
Beispiele: das Login bei Google mit Passwort und Code aus der Authenticator-App, die Bankkarte mit PIN, das E-Banking mit Passwort und Freigabe in der App.

## 3FA
**Drei-Faktor-Authentifizierung** kombiniert alle drei Kategorien: Wissen, Besitz und Inhärenz.
Beispiele: der Zutritt zu Rechenzentren oder militärischen Anlagen mit Badge, PIN und Fingerabdruck; ein Hardware-Token mit Fingerprint-Sensor zusammen mit einem Passwort. 3FA kommt vor allem in Hochsicherheitsbereichen zum Einsatz, im Alltag ist sie selten.

## Methoden im Vergleich
| Methode | Sicherheit | Bemerkung |
|---|---|---|
| SMS-Code | ⭐ | Anfällig für SIM-Swapping und Abfangen. Besser als nichts. |
| E-Mail-Code | ⭐ | Nur so sicher wie das E-Mail-Konto |
| TOTP-App (Google/Microsoft Authenticator, Aegis, 2FAS) | ⭐⭐⭐ | Zeitbasierte 6-stellige Codes (RFC 6238), funktioniert offline |
| Push-Bestätigung | ⭐⭐⭐ | Bequem, aber Gefahr der «MFA-Fatigue» (Push-Bombing) |
| Hardware-Key FIDO2 / U2F (YubiKey) | ⭐⭐⭐⭐ | **Phishing-resistent**, weil der Key an die Domain gebunden ist |
| Passkeys | ⭐⭐⭐⭐ | Kombination aus Gerät (Besitz) und Biometrie oder PIN. Phishing-resistent und ganz ohne Passwort. |

## Vor- und Nachteile
**Vorteile**
- Ein gestohlenes Passwort allein genügt nicht mehr. Laut Microsoft verhindert MFA über 99 % der automatisierten Kontoangriffe.
- Schützt vor Credential Stuffing nach Passwort-Leaks.

**Nachteile**
- Etwas weniger komfortabel
- Bei Verlust des Geräts droht der Ausschluss aus dem Konto. **Wiederherstellungscodes** sicher aufbewahren, zum Beispiel im Passwortmanager oder ausgedruckt.
- Echtzeit-Phishing (Adversary-in-the-Middle) kann SMS- und TOTP-Codes abfangen. Nur FIDO2 und Passkeys schützen davor.

## Meine Konten mit MFA
| Dienst | MFA aktiv? | Methode |
|---|---|---|
| ✏️ TODO (z. B. Microsoft/TBZ) | | |
| ✏️ TODO (z. B. Google) | | |
| ✏️ TODO (z. B. Instagram) | | |
| GitHub | | |
