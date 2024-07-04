# 🤖 Agderposten 20 Spørsmål formaterer

Dette scriptet er laget for å formatere "20 spørsmåls" filer til 2 x 10 spørsmål til bruk i Agderposten. 

- Scriptet leser .txt filer fra mappen "unformatted" (eller annet navn gitt i format.py) ⬇️.
- Deretter lager den en formatert kopi i mappen kalt "formatted" (kan også bytte navn i format.py) ⬆️

> Noen filer slipper iblant gjennom med feil, disse blir som regel markert med "_manual" i filnavnet. 


# 📦 For å kjøre:
Programmet kan kun kjøres med .bat filen fra Windows PCer, men kan kjøres fra terminal i Windows, Mac og Linux

### Struktur

```
agp_question_formater-main
├── formater.py
├── run_windows.bat
├── unformatted
│   └── 📄 Plasser uformaterte .txt filer her <----
└── formatted
    └── 📁 Denne mappen genereres automatisk vis den ikke er tilstede. Her kommer output.
```



### Stegvis
+ Ha python installert lokalt på maskinen din: https://www.python.org/downloads/
+ Trykk på grønn `<>Code` knapp oppe til høyre, og trykk "Download ZIP"
+ Pakk ut zip filen.  
+ Legg filer som skal formateres inn i "unformatted" mappen.
+ Kjør (dobbelttrykk) vedlagt .bat fil
+ Filene skal nå ligge i `formatted` mappen. Disse kan du nå bruke i AGP :D

> NB! Scriptet er ikke grundig testet og derfor burde det alltid dobbeltsjekkes at spørsmål og svar er riktig! 


