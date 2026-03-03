# Git - Github Tutorial for collaborative work in Ignition

[Git Official Documentation](https://git-scm.com/docs)

Acest document este un ghid rapid pentru a înțelege cum folosim Git pentru a lucra în echipă pe proiectele din Ignition fără să ne suprascriem munca unii altora.

## Comenzi de bază (The Bread & Butter)

- [**init**](https://git-scm.com/docs/git-init) - Inițializează un repository nou. Transformă un folder normal într-unul monitorizat de Git.
- [**config**](https://git-scm.com/docs/git-config) - Setează datele tale (`user.name` / `user.email`). Esențial pentru a ști exact cine a stricat sau a reparat un fișier.
- [**add**](https://git-scm.com/docs/git-add) - Adaugă fișierele modificate în "staging area". E ca și cum ai pune produsele în coș înainte să mergi la casa de marcat.
- [**commit**](https://git-scm.com/docs/git-commit) - Salvează modificările din "staging" cu un mesaj descriptiv. (Ex: `git commit -m "Reparat butonul de start"`). E practic o salvare a jocului (save state).
- [**branch**](https://git-scm.com/docs/git-branch) - Creează o ramură nouă. Regula de aur: **Nu lucrăm direct pe master!** Fiecare feature sau bug primește propriul branch.
- [**checkout** / **switch**](https://git-scm.com/docs/git-checkout) - Te mută de pe un branch pe altul. Atenție: fișierele de pe hard drive (și din Ignition) se vor schimba automat când faci asta!

---

## Sincronizarea cu serverul (GitHub)

- [**remote**](https://git-scm.com/docs/git-remote) - Conectează repo-ul tău local cu cel de pe GitHub.
- [**push**](https://git-scm.com/docs/git-push) - Trimite commit-urile tale locale pe serverul GitHub pentru a le vedea și restul echipei.
- [**fetch**](https://git-scm.com/docs/git-fetch) - Descarcă istoricul nou de pe server, dar **nu** modifică fișierele tale locale. E doar pentru a vedea "ce a mai apărut nou".
- [**pull**](https://git-scm.com/docs/git-pull) - Face `fetch` + `merge` automat. Aduce modificările de pe server și le combină cu codul tău.

---

## Avansat: Combinarea codului

- [**merge**](https://git-scm.com/docs/git-merge) - Combină un branch (ex: `feature/change_gauge`) în branch-ul principal (`master`).
- [**rebase**](https://git-scm.com/docs/git-rebase) - O alternativă la merge care rescrie istoricul pentru a păstra totul pe o singură linie dreaptă. (Folosiți cu mare atenție, niciodată pe branch-uri publice!).

---

## Studiu de caz: Cum arată un Merge Conflict rezolvat

Priviți acest istoric real generat de comanda `git log --oneline --graph`:

```text
* 46f09ba (HEAD -> master, origin/master) Merge branch 'feature/change_gauge_color'
|\  
| * 407e222 (origin/feature/change_gauge_color) feat: Changed styling for Simple_Gauge
* | 6722c2d feat: Style Change (This will cause merge conflict next)
|/  
* cde4c97 Project init
* 81bf81b Added gitignore
```

---

## Ce s-a întâmplat aici?

1. Am pornit de la baza comună (cde4c97 Project init).
2. Cineva a creat branch-ul feature/change_gauge_color și a modificat un fișier (commit 407e222).
3. În același timp, altcineva a modificat același fișier direct pe master (commit 6722c2d).
4. Când s-a încercat unirea (merge), Git a dat eroare de Merge Conflict pentru că nu știa ce variantă să aleagă.
5. Conflictul a fost rezolvat manual de un om, rezultând commit-ul de unire 46f09ba.

---

## Part 2

## Convenții pentru Numele Branch-urilor (Best Practices)

Pentru a lucra eficient în echipă și a înțelege imediat ce face fiecare ramură, folosim următoarele prefixe standard:

- **`feat/`** -> Pentru funcționalități și ecrane noi (ex: `feat/adaugare-pompe-apa`).
- **`fix/`** -> Pentru repararea erorilor sau bug-urilor (ex: `fix/eroare-script-motor`).
- **`docs/`** -> Pentru actualizări de documentație (ex: `docs/update-readme`).
- **`test/`** -> Pentru teste experimentale.

---

## Git Stash (Sertarul cu ciorne)

**Scenariu Ignition:** Lucrezi la un ecran complex de Perspective. Deodată, un coleg te roagă să verifici o problemă pe ramura `master`. Nu poți face `commit` pentru că ecranul tău e pe jumătate stricat, dar nici nu vrei să pierzi munca.

Soluția este să "ascunzi" temporar modificările tale folosind `stash`.

```bash
# 1. Salvezi munca neterminată în "sertar"
git stash -m "Jumătate de ecran Perspective terminat"

# 2. Acum folderul e curat. Te muți pe master să îți ajuți colegul
git checkout master
git pull

# 3. Rezolvi problema, te întorci pe branch-ul tău
git checkout feat/ecran-nou

# 4. Scoți munca din sertar și continui de unde ai rămas
git stash pop
```

---

## Pull Requests (PR) și Code Review
Nu dăm niciodată `merge` direct în `master` de capul nostru. Când termini de lucrat pe branch-ul tău, ceri permisiunea ca altcineva să valideze modificările tale (mai ales scripturile de Python).

### Fluxul corect de lucru:

- Trimiți codul tău pe server: `git push origin feat/numele-feature`
- Intri pe GitHub și apeși butonul verde **Compare & pull request.**
- Un coleg verifică modificările.
- Dacă totul este corect și nu crapă nimic, el aprobă (Approve) și dă **Merge PR.**

## Combinarea Codului: Merge vs. Rebase

### Git Merge
Combină un branch (ex: `feat/change_gauge`) în branch-ul principal (`master`), creând un "Merge Commit" care unește cele două istorii.

### Studiu de caz: Cum arată un Merge Conflict rezolvat
Dacă doi oameni modifică același fișier, Git se oprește și îți cere să rezolvi manual conflictul. Iată cum arată în istoric:

```text
* 46f09ba (HEAD -> master) Merge branch 'feat/change_gauge'
|\  
| * 407e222 feat: Changed styling for Simple_Gauge
* | 6722c2d feat: Style Change (This caused the conflict)
|/  
* cde4c97 Project init
```

## Git Rebase (Păstrarea unui istoric curat)
**Scenariu:** Tu lucrezi de o săptămână la feat/alarme. Între timp, colegii au băgat mult cod nou pe master. Vrei ca branch-ul tău să conțină cel mai nou cod, dar fără să creezi un "merge commit" haotic. Rebase mută efectiv commit-urile tale la capătul noului master.

```bash
# 1. Actualizezi master-ul local
git checkout master
git pull

# 2. Te întorci pe branch-ul tău
git checkout feat/alarme

# 3. Muta baza branch-ului tău la capătul master-ului
git rebase master
```

**Regula de Aur: NICIODATĂ nu faceți rebase pe un branch public (ex: `master`). Rebase rescrie istoria! Folosiți-l doar pe branch-urile voastre locale.**

## Butoanele de Panică (Cum repari când ai stricat ceva)

1. `git restore` **(Am stricat, dă-mi înapoi versiunea veche)**
Ai modificat un script, ai dat Save în Ignition Designer, ți-ai dat seama că ai distrus tot, dar **nu ai făcut încă commit.**

```Bash
# Anulează modificările dintr-un fișier anume:
git restore <cale_fisier>

# Opțiunea Nucleară: Anulează ABSOLUT TOATE modificările nesalvate:
git restore .
```

2. `git reset` (Am făcut un commit local greșit)
Ai dat `git commit`, dar ai uitat să adaugi un fișier sau ai greșit mesajul. (Condiție: **Nu ai dat încă push** pe GitHub).

```bash
# Șterge ultimul commit, dar PĂSTREAZĂ modificările tale în fișiere:
git reset --soft HEAD~1

# Opțiunea Nucleară: Șterge ultimul commit ȘI ȘTERGE definitiv modificările:
git reset --hard HEAD~1
```

3. git revert **(Am făcut push la o prostie, producția e picată)**

Ai făcut commit, ai dat push pe GitHub, iar codul a ajuns pe master și a stricat proiectul. Trebuie să anulezi ce ai făcut public, dar lăsând o urmă clară a reparației.

```bash
# Creează un commit NOU care face exact opusul commit-ului greșit:
git revert <ID_Commit_Gresit>
```