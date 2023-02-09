import re
import csv

regeln = [(re.compile(regel), ziel) for regel, ziel in [
    (r"\bDerma", "Dermatologie"),
    (r"\bUrolog", "Urologie"),
    (r"\bNeurolog", "Neurologie"),
    (r"(?i)\bPsych", "Psychiatrie"),
    (r"(?i)Anästhes|Schmerzth", "Anästhesie"),
    (r"\bAugen|\bOphth", "Augenheilkunde"),
    (r"(?i)radiolog", "Radiologie"),
    (r"(?i)\bStrahlent|Nuklearmed", "Strahlentherapie"),
    (r"\bHNO|\bOhren", "HNO"),
    (r"\bGynäko|\bGeburtshil|\bFrauenheil|Frauenklin", "Gynäkologie"),
    (r"(?i)\bPädiatrie|\bKinder(?!.*chirurgie)", "Pädiatrie"),
    (r"(?i)\bKiefer|\bZahn", "Zahnheilkunde"),
    (r"(?i)Orthopäd|Chirurgi", "Chirurgie"),
    (r"(?i)\bInnere|kardiologi|pneumologi|\bpulmo|hämatologi|onkologi|infektio|angiologi|endokrinologi|\bpneumologi|palliati|phlebolo|geriatr", "Innere Medizin"),
    (r"\bIntensivmed", "Anästhesie"),
    ] 
]

with open("Abteilungsliste.txt", encoding="cp1252") as abt_liste:
    abteilungen = [zeile.strip() for zeile in abt_liste]

with open("Abteilungen.csv", "w", newline="") as csv_ausgabe:
    writer = csv.writer(csv_ausgabe, delimiter=";")
    writer.writerow(["Abteilung", "Zuordnung"])
    for abteilung in abteilungen:
        for regel in regeln:
            if regel[0].search(abteilung):
                writer.writerow([abteilung, regel[1]])
                break
        else:
            writer.writerow([abteilung, "Sonstige"])



