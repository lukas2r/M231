# Git-Repository für das persönliche Dossier

## Mein Repository
- **URL:** https://github.com/lukas2r/M231
- **Plattform:** GitHub
- **Sichtbarkeit:** ✏️ TODO (empfohlen: **privat**, nur du und die Lehrperson haben Zugriff)
- **Lehrperson eingeladen:** ✏️ TODO (GitHub-Benutzername der Lehrperson, Datum)

## Lehrperson einladen
1. Repo öffnen → **Settings** → **Collaborators** (bzw. *Collaborators and teams*)
2. **Add people** → Benutzername oder E-Mail-Adresse der Lehrperson eingeben → Rolle *Read* reicht
3. Die Lehrperson muss die Einladung annehmen.

> Falls die Lehrperson GitLab verlangt: auf gitlab.com ein Projekt erstellen → *Manage → Members → Invite members* (Rolle *Reporter*), oder das GitHub-Repo über *New project → Import project → GitHub* importieren.

## Wichtige Git-Befehle
```bash
git clone https://github.com/lukas2r/M231.git   # Repo lokal holen
git status                                       # Änderungen anzeigen
git add .                                        # Änderungen vormerken (stagen)
git commit -m "LB1: Cookies ergänzt"             # Lokal festhalten
git push                                         # Auf GitHub hochladen
git pull                                         # Neueste Version holen
git log --oneline                                # Verlauf anzeigen
```

## Sicherheit beim Arbeiten mit Git
- **Keine Passwörter, Schlüssel oder privaten PGP-Keys** committen. Einmal gepusht, bleiben sie in der Historie, auch wenn man sie später löscht.
- Für die Anmeldung einen **Personal Access Token** oder SSH-Key statt eines Passworts verwenden und **2FA** auf GitHub aktivieren.
- Auf Screenshots persönliche Daten (Adresse, Ausweis, Passwörter) unkenntlich machen.
- Eine `.gitignore`-Datei für temporäre Dateien verwenden.

## Struktur dieses Dossiers
Siehe [README](../README.md).
