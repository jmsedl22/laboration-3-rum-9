# Laboration 4

## Följ en CSV-rad genom programmet
- *Var läses raden?* Den läses på rad 10.
- *Hur hämtas värdena från raden?* Den läses av via en csv-reader.
- *Var skapas instansen?* Instansen av SupportCase skapas på rad 12, inuti en for-loop.
- *Hur hamnar värdena i instansens attribut?* De initieras via anropet till dess konstruktor.
- *Var sparas den färdiga instansen?* Den sparas i en lista med SupportCases som kallas cases.
- *Hur används instansen senare i programmet?* Den används senare för att skriva ut/returnera information om supportärendet.

## Förberedelse för diskussion

- *Vad döpte ni klassen till?* SupportCase på engelska enligt Python-konvention.
- *Vilka attribut valde ni?* Samma attribut som kolumnerna i filen.
- *Vilken metod skapade ni?* read_cases(), som läser supportärenden från en csv-fil.
- *Vad placerade ni i klassen och vad placerade ni utanför den?* Vi lade en describe()-funktion som skriver ut info om objektet i terminalen. Vi lade inte read_cases() i filen, eftersom det har att göra med filinläsning och inte med objektet i sig.
