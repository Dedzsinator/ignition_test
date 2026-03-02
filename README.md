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

## Sincronizarea cu serverul (GitHub)

- [**remote**](https://git-scm.com/docs/git-remote) - Conectează repo-ul tău local cu cel de pe GitHub.
- [**push**](https://git-scm.com/docs/git-push) - Trimite commit-urile tale locale pe serverul GitHub pentru a le vedea și restul echipei.
- [**fetch**](https://git-scm.com/docs/git-fetch) - Descarcă istoricul nou de pe server, dar **nu** modifică fișierele tale locale. E doar pentru a vedea "ce a mai apărut nou".
- [**pull**](https://git-scm.com/docs/git-pull) - Face `fetch` + `merge` automat. Aduce modificările de pe server și le combină cu codul tău.

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

## Ce s-a întâmplat aici?

1. Am pornit de la baza comună (cde4c97 Project init).
2. Cineva a creat branch-ul feature/change_gauge_color și a modificat un fișier (commit 407e222).
3. În același timp, altcineva a modificat același fișier direct pe master (commit 6722c2d).
4. Când s-a încercat unirea (merge), Git a dat eroare de Merge Conflict pentru că nu știa ce variantă să aleagă.
5. Conflictul a fost rezolvat manual de un om, rezultând commit-ul de unire 46f09ba.

## COMING SOON

- stash
- branch conventions
- pr
- rebase
- restore, revert, reset
