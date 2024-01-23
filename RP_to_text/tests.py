text = """
Support : Ecrit Type : Insertion publicitaire Tags : TPME / financement / banque

Titre : Les Assises Régionales du Financement par Tamwilcom

Journal : LE MATIN
"""

rows = text.strip().split('\n')
rows = [row for row in rows if row.strip()]
print(rows[0].split()[0] == 'Support' and rows[1].split()[0] == 'Titre')
print(rows[0])
print(rows[1])