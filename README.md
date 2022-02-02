# Istruzioni per usare git con questo progetto

Per prima cosa clonate il repository:
```
git clone https://github.com/zanocrate/LCP_projects_Y4.git
```
Questo creerà una cartella `LCP_projects_Y4` nella directory dove avete eseguito questo comando. Entrandoci con `cd LCP_projects_Y4`, prima di mettervi al lavoro e fare qualsiasi cosa fate
```
git fetch origin
git merge
```

Così sarete aggiornati all'ultimo commit che è stato fatto, visto che non lavoriamo su branch diverse per comodità. Ora fate le modifiche che dovete fare, controllate con `git status` cosa aggiungere al commit con `git add` (se fate `git add *` o `git add .` vi aggiungerà automaticamente tutto, tranne i file che decidiamo di ignorare in `.gitignore`), poi fate

```
git commit -m "commento al commit"
git push origin
```
A questo punto vi chiederà le credenziali per poter eseguire il push, inserite il vostro account di github e dovrebbe funzionare.
Se volete evitare di inserire le credenziali ogni volta, vi basta eseguire questo comando prima del push:

```
git config credential.helper store
git push origin
```

Questo salverà le vostre credenziali *in chiaro* localmente in un file chiamato `.git-credentials`.
