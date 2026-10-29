# Webseite verwendet Cookies

## Was ist ein Cookie?
Ein Cookie ist eine kleine Textdatei bzw. ein Name-Wert-Paar, das ein Webserver im Browser speichert. Der Browser sendet es bei jeder weiteren Anfrage an dieselbe Domain automatisch mit. HTTP ist **zustandslos**. Erst Cookies ermöglichen es, sich zu «merken», wer man ist, zum Beispiel für ein Login oder einen Warenkorb.

## Funktionsweise
```
1. Browser  → GET /login                       → Server
2. Browser  ← 200 OK  Set-Cookie: session=ab12; HttpOnly; Secure  ← Server
3. Browser  → GET /konto   Cookie: session=ab12 → Server   (Server erkennt den Benutzer)
```
Wichtige Attribute: `Expires`/`Max-Age` (Lebensdauer), `Domain`, `Path`, `Secure` (nur über HTTPS), `HttpOnly` (kein Zugriff per JavaScript), `SameSite` (Schutz vor CSRF).

## Arten von Cookies
| Art | Beschreibung | Einwilligung nötig? |
|---|---|---|
| **Session-Cookie** | Wird beim Schliessen des Browsers gelöscht | – |
| **Persistentes Cookie** | Hat ein Ablaufdatum und bleibt bis dahin gespeichert | – |
| **First-Party** | Stammt von der besuchten Domain | – |
| **Third-Party** | Stammt von einer fremden Domain (z. B. Werbenetzwerk). Ermöglicht seitenübergreifendes Tracking. | ja |
| **Notwendig / technisch** | Login, Warenkorb, Spracheinstellung, Cookie-Einwilligung | nein |
| **Präferenzen / Funktional** | Komfortfunktionen | in der EU in der Regel ja |
| **Statistik / Analyse** | z. B. Google Analytics | ja (EU) |
| **Marketing / Tracking** | Personalisierte Werbung, Profilbildung | ja |

## Wieso braucht es Cookie-Banner?
- **EU**: Die ePrivacy-Richtlinie und die DSGVO verlangen eine **vorgängige, informierte und freiwillige Einwilligung (Opt-in)** für alle Cookies, die nicht technisch notwendig sind. «Ablehnen» muss genauso einfach sein wie «Akzeptieren».
- **Schweiz**: Art. 45c FMG und das DSG verlangen grundsätzlich nur eine **Information** und eine Möglichkeit zum Widerspruch (Opt-out). Schweizer Websites, die sich an EU-Besucher richten, müssen jedoch die DSGVO einhalten. Deshalb haben die meisten Schweizer Websites ebenfalls Banner.
- **Sinn und Zweck**: Transparenz und Selbstbestimmung. Der Nutzer soll entscheiden können, ob sein Surfverhalten verfolgt wird.

## Problematik
- «Dark Patterns»: Der Akzeptieren-Knopf ist farbig hervorgehoben, das Ablehnen ist versteckt.
- Banner-Müdigkeit führt dazu, dass Nutzer alles akzeptieren.
- Auch ohne Cookies wird getrackt: Browser-Fingerprinting, Tracking-Pixel, Local Storage.

## Selbstschutz
- In Banners «Nur notwendige» wählen
- Drittanbieter-Cookies im Browser blockieren, Tracking-Schutz aktivieren (Firefox, Brave)
- Erweiterungen wie uBlock Origin
- Cookies regelmässig löschen oder den privaten Modus verwenden

## Praxis: Cookies im Browser anschauen
✏️ **TODO**: Öffne die Entwicklertools (F12) → *Application/Speicher* → *Cookies* auf einer Website deiner Wahl, zum Beispiel 20min.ch. Füge einen Screenshot ein und notiere, wie viele Drittanbieter-Cookies du gefunden hast.
