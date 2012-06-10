# -*- coding: utf-8 -*-

{
    "name": "Inserisce sugli Articoli il codice Articolo Ad-Hoc Zucchetti ",
    "version": "1.01",
    "depends": ["product"],
    "author": "C & G Software S.a.s.",
    "category": "Product",
    "description": """Permette di salvare il codice articolo Ad-Hoc Windows Sugli Articoli
    """,
    "init_xml": [],
    'update_xml': [
                   'adhoc_code.xml',
                   # 'security/ir.model.access.csv',
                   ],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': '${certificate}',
}
