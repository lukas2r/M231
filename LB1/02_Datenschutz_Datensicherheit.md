# Datenschutz vs. Datensicherheit

## Definitionen
**Datenschutz** schützt die **Person** vor einer missbräuchlichen Bearbeitung ihrer Personendaten. Es geht um das Recht auf informationelle Selbstbestimmung und Privatsphäre. Die Frage lautet: *Darf* man diese Daten überhaupt bearbeiten, und wenn ja, wie?
→ Grundlage ist das Gesetz (DSG), es handelt sich also um ein **rechtliches** Thema.

**Datensicherheit** schützt die **Daten selbst**, und zwar alle Daten, nicht nur Personendaten, vor Verlust, Manipulation und unberechtigtem Zugriff. Die Frage lautet: *Wie* schütze ich die Daten technisch und organisatorisch?
→ Es handelt sich um ein **technisch-organisatorisches** Thema.

## Schutzziele der Datensicherheit (CIA-Triade)
| Schutzziel | Bedeutung | Beispielmassnahme |
|---|---|---|
| **Vertraulichkeit** (Confidentiality) | Nur Berechtigte haben Zugriff. | Verschlüsselung, Zugriffsrechte |
| **Integrität** (Integrity) | Die Daten sind unverändert und korrekt. | Hashwerte, digitale Signaturen |
| **Verfügbarkeit** (Availability) | Die Daten sind bei Bedarf zugänglich. | Backups, Redundanz (RAID), USV |

Ergänzend nennt man oft auch Authentizität und Nachvollziehbarkeit (Verbindlichkeit).

## Zusammenhang
Ohne Datensicherheit gibt es keinen Datenschutz. Das DSG verlangt in Art. 8 ausdrücklich «angemessene technische und organisatorische Massnahmen». Datensicherheit ist also ein **Mittel**, um Datenschutz zu erreichen. Umgekehrt betrifft Datensicherheit auch Daten ohne Personenbezug, etwa Geschäftsgeheimnisse oder Quellcode.

```
      Datenschutz (Was ist erlaubt? → Person)
            ▲
            │ setzt voraus
            │
      Datensicherheit (Wie schützen? → Daten)
```

## Beispiele
| Situation | Datenschutz | Datensicherheit |
|---|---|---|
| Eine Firma verkauft Kundenadressen ohne Einwilligung an Dritte. | ✅ verletzt | – |
| Die Festplatte mit der Buchhaltung geht kaputt, es gibt kein Backup. | – | ✅ verletzt (Verfügbarkeit) |
| Ein Hacker stiehlt die unverschlüsselte Patientendatenbank. | ✅ verletzt | ✅ verletzt (Vertraulichkeit) |
| Eine Videoüberwachung filmt das Nachbargrundstück. | ✅ verletzt | – |
| Ein Angreifer manipuliert Preise im Webshop. | – | ✅ verletzt (Integrität) |
| Eine Mitarbeiterin lässt ihren PC ungesperrt, ein Kollege liest Lohndaten. | ✅ | ✅ |
