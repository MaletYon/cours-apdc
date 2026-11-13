"""Métadonnées des cours et répartition des 15 séances de 2 heures."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

GCI = {
    "sigle": "GCI",
    "code": "MSN-2S3-MSI03",
    "titre": "IT Governance, COBIT et ITIL",
    "sous_titre": "Gouverner, piloter et servir : la gouvernance des systèmes d'information en contexte africain",
    "master": "Master professionnel en Management des Systèmes d'Information · Semestre 3",
    "annee": "2026-2027",
    "dossier": COURS + r"\Chaire-Unesco\MSN-2S3-MSI03\Présentation",
    "fil_rouge": "BANQUE SANAGA (Douala), KRIBILOG (Kribi), ANPP (administration), NOUN PAY (fintech)",
    "parties": [
        ("Prologue", "Trois jours sans banque", "P00"),
        ("Partie I", "Fondements de la gouvernance des SI", "C01–C04"),
        ("Partie II", "COBIT 2019 : le référentiel de la gouvernance", "C05–C08"),
        ("Partie III", "Cadre normatif, juridique et déontologique", "C09–C11"),
        ("Partie IV", "ITIL 4 et pratique opérationnelle", "C12–C17"),
        ("Partie V", "Défis avancés et émergents", "C18–C19"),
        ("Partie VI", "Recherche et contributions", "C20"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · Trois jours sans banque", "Présentation du cours + Prologue", ["P00"], []),
        2: ("De la gouvernance d'entreprise à la gouvernance des SI", "C01", ["C01"], []),
        3: ("Grandes défaillances · Alignement stratégique", "C02 + C03 §1-2", ["C02"], []),
        4: ("Valeur, décision · Panorama des référentiels", "C03 §3-6 + C04 §1-3", ["C03"], ["LAB-01"]),
        5: ("Carte des référentiels · COBIT 2019 : principes", "C04 §4-6 + C05", ["C04", "C05"], []),
        6: ("Les 40 objectifs de COBIT 2019", "C06 + C07 §1", ["C06"], ["LAB-03"]),
        7: ("Concevoir et mesurer : facteurs, capacité, feuille de route", "C07 §2-5 + C08", ["C07", "C08"], ["LAB-02", "LAB-04"]),
        8: ("Normes internationales · Cadre juridique (1)", "C09 + C10 §1-2", ["C09"], []),
        9: ("Cadre juridique (2) · Audit et assurance (1)", "C10 §3-8 + C11 §1-2", ["C10"], []),
        10: ("Audit et assurance (2) · ITIL 4 : le système de valeur", "C11 §3-6 + C12", ["C11", "C12"], ["LAB-05"]),
        11: ("Incidents, problèmes, demandes · Changements (1)", "C13 + C14 §1-2", ["C13"], ["LAB-06"]),
        12: ("Mises en production, configuration · Niveaux de service", "C14 §3-5 + C15", ["C14", "C15"], ["LAB-07", "LAB-08"]),
        13: ("Processus, RACI, mesure · Cas intégrateurs (1)", "C16 + C17 cas 1-2", ["C16"], ["LAB-09"]),
        14: ("Cas intégrateurs (2) · Agilité, DevOps et cloud", "C17 cas 3-4 + C18", ["C17", "C18"], ["LAB-10"]),
        15: ("Données et IA · Recherche · Clôture", "C19 + C20 + synthèse", ["C19", "C20"], []),
    },
}

ACSI = {
    "sigle": "ACSI",
    "code": "MSN-2S3-MSI05",
    "titre": "Audit et Contrôle Interne des SI",
    "sous_titre": "Méthode, normes et pratique de la mission d'audit : du métier à l'auditologie",
    "master": "Master professionnel en Management des Systèmes d'Information · Semestre 3",
    "annee": "2026-2027",
    "dossier": COURS + r"\Chaire-Unesco\MSN-2S3-MSI05\Présentation",
    "fil_rouge": "LiZbiZ, BANQUE SANAGA, ANPP",
    "parties": [
        ("Prologue", "Quarante-cinq questions", "P00"),
        ("Partie I", "Fondements de l'audit et du contrôle interne", "C01–C04"),
        ("Partie II", "Méthode de la mission d'audit", "C05–C09"),
        ("Partie III", "Cadre normatif, juridique et déontologique", "C10–C12"),
        ("Partie IV", "Pratique de l'audit des SI", "C13–C18"),
        ("Partie V", "Défis avancés", "C19–C20"),
        ("Partie VI", "Recherche : l'auditologie", "C21–C22"),
    ],
    "jours": {
        1: ("Ouverture · Quarante-cinq questions", "Présentation du cours + Prologue", ["P00"], []),
        2: ("Auditer, contrôler, donner une assurance · Contrôle interne (1)", "C01 + C02 §1-2", ["C01"], []),
        3: ("Contrôle interne (2) · Le risque et sa cartographie", "C02 §3-7 + C03", ["C02", "C03"], ["LAB-01", "LAB-02"]),
        4: ("La fraude · La mission d'audit (1)", "C04 + C05 §1-2", ["C04"], []),
        5: ("La mission d'audit (2) · Préparer et planifier", "C05 §3-5 + C06", ["C05", "C06"], ["LAB-03"]),
        6: ("Décomposer l'espace d'audit · Collecter la preuve (1)", "C07 + C08 §1-4", ["C07"], ["LAB-04"]),
        7: ("Collecter la preuve (2) · Conclure", "C08 §5-6 + C09", ["C08", "C09"], ["LAB-05"]),
        8: ("Les normes professionnelles de l'audit", "C10 + C11 §1", ["C10"], []),
        9: ("Référentiels de contrôle · Cadre juridique (1)", "C11 §2-5 + C12 §1-4", ["C11"], []),
        10: ("Cadre juridique (2) · Auditer la gouvernance et la DSI", "C12 §5-6 + C13", ["C12", "C13"], ["LAB-06"]),
        11: ("Auditer une application · Auditer les projets (1)", "C14 + C15 §1-3", ["C14"], ["LAB-07"]),
        12: ("Projets (2) · Sécurité et infrastructure · Production (1)", "C15 §4 + C16 + C17 §1-2", ["C15", "C16"], ["LAB-08"]),
        13: ("Continuité et tiers · Cas intégrateurs", "C17 §3-4 + C18", ["C17", "C18"], ["LAB-09", "LAB-10"]),
        14: ("Audit continu, outils · Auditer l'IA", "C19 + C20", ["C19", "C20"], []),
        15: ("L'auditologie · Mesurer l'incertitude · Clôture", "C21 + C22 + synthèse", ["C21", "C22"], []),
    },
}

ALL = {"GCI": GCI, "ACSI": ACSI}

NRAC = {
    "sigle": "NRAC",
    "code": "MSN-2S3-SEC08",
    "titre": "Normes, gestion des risques et audit de cybersécurité",
    "sous_titre": "Du référentiel à la preuve : piloter, mesurer et auditer la sécurité",
    "master": "Master professionnel en Sécurité des Systèmes Numériques · Semestre 3",
    "annee": "2026-2027",
    "dossier": COURS + r"\Chaire-Unesco\MSN-2S3-SEC08\Présentation",
    "fil_rouge": "BANQUE SANAGA (Douala), LiZbiZ (logistique), ANPP (administration)",
    "parties": [
        ("Prologue", "Certifiée, et pourtant compromise", "P00"),
        ("Partie I", "Fondements", "C01–C02"),
        ("Partie II", "Méthodes : risque et audit", "C03–C07"),
        ("Partie III", "Cadre normatif, juridique et déontologique", "C08–C10"),
        ("Partie IV", "Pratique", "C11–C14"),
        ("Partie V", "Défis avancés", "C15"),
        ("Partie VI", "Recherche", "C16"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · Certifiée, et pourtant compromise", "Présentation du cours + Prologue", ["P00"], []),
        2: ("Gouverner la cybersécurité : du contrôle à la GRC", "C01", ["C01"], []),
        3: ("Le risque cyber : notions, mesure, incertitude", "C02", ["C02"], ["LAB-01"]),
        4: ("Gérer les risques : ISO 31000 et ISO/IEC 27005", "C03", ["C03"], []),
        5: ("EBIOS Risk Manager", "C04", ["C04"], ["LAB-02", "LAB-03"]),
        6: ("Quantifier le risque cyber : FAIR", "C05", ["C05"], ["LAB-04"]),
        7: ("Conduire un audit de cybersécurité", "C06", ["C06"], []),
        8: ("Décomposer, coter, conclure", "C07", ["C07"], ["LAB-05"]),
        9: ("La famille ISO/IEC 27000", "C08", ["C08"], ["LAB-06"]),
        10: ("Les autres référentiels et leurs correspondances", "C09", ["C09"], ["LAB-07"]),
        11: ("Le cadre camerounais et africain, la déontologie", "C10", ["C10"], []),
        12: ("Mettre en œuvre et auditer un SMSI", "C11", ["C11"], ["LAB-08"]),
        13: ("L'audit technique de sécurité", "C12", ["C12"], ["LAB-09"]),
        14: ("La GRC en pratique · Études de cas intégratrices", "C13 + C14", ["C13", "C14"], ["LAB-10"]),
        15: ("Risques émergents · Mesurer ce que l'on ne sait pas · Clôture", "C15 + C16 + synthèse", ["C15", "C16"], []),
    },
}

ALL["NRAC"] = NRAC

FAV = {
    "sigle": "FAV",
    "code": "MSN-2S3-SEC07",
    "titre": "Forensics et analyse de vulnérabilités",
    "sous_titre": "Expliquer l'incident, empêcher le suivant : de la trace à la correction vérifiée",
    "master": "Master professionnel en Sécurité des Systèmes Numériques · Semestre 3",
    "annee": "2026-2027",
    "dossier": COURS + r"\Chaire-Unesco\MSN-2S3-SEC07\Présentation",
    "fil_rouge": "NYANGA CRÉDIT (Bafoussam), SOLITRANS LOGISTIQUE (Douala)",
    "parties": [
        ("Prologue", "La nuit du 14 mars à Bafoussam", "P00"),
        ("Partie I", "Fondements", "C01–C02"),
        ("Partie II", "Méthode : examiner les supports", "C03–C07"),
        ("Partie III", "Cadre normatif et juridique", "C08"),
        ("Partie IV", "Pratique : les vulnérabilités", "C09–C12"),
        ("Partie V", "Défis avancés", "C13–C15"),
        ("Partie VI", "Recherche", "C16"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ("Ouverture · La nuit du 14 mars · L'investigation numérique", "Présentation + P00 + C01", ["P00", "C01"], []),
        2: ("La preuve numérique et la chaîne de possession", "C02", ["C02"], ["LAB-01"]),
        3: ("Acquérir et préserver", "C03", ["C03"], ["LAB-02"]),
        4: ("L'analyse du disque", "C04", ["C04"], ["LAB-03"]),
        5: ("L'analyse de la mémoire", "C05", ["C05"], ["LAB-04"]),
        6: ("L'analyse du réseau", "C06", ["C06"], ["LAB-05"]),
        7: ("Chronologie et corrélation", "C07", ["C07"], ["LAB-06"]),
        8: ("Normes et droit de la preuve numérique", "C08", ["C08"], []),
        9: ("Qu'est-ce qu'une vulnérabilité", "C09", ["C09"], ["LAB-08"]),
        10: ("Identifier les vulnérabilités sans les exploiter", "C10", ["C10"], ["LAB-07"]),
        11: ("Gérer les vulnérabilités", "C11", ["C11"], ["LAB-09"]),
        12: ("De l'artefact à la vulnérabilité", "C12", ["C12"], []),
        13: ("Anti-forensique et nuage", "C13", ["C13"], []),
        14: ("L'enquête intégratrice", "C14", ["C14"], ["LAB-10"]),
        15: ("Le rapport et le témoignage · Mesurer l'incertitude · Clôture", "C15 + C16", ["C15", "C16"], []),
    },
}

ALL["FAV"] = FAV

APDC = {
    "sigle": "APDC",
    "code": "MSN-2S4-SEC02",
    "titre": "Audit de protection des données et conformité",
    "sous_titre": "Prouver la conformité, protéger les personnes : auditer l'application de la loi n° 2024/017",
    "master": "Master professionnel en Sécurité des Systèmes Numériques · Semestre 4",
    "annee": "2026-2027",
    "dossier": COURS + r"\Chaire-Unesco\MSN-2S4-SEC02\Présentation",
    "fil_rouge": "NYANGA CRÉDIT (Bafoussam), CENTRE MÉDICAL MBOLO (Bertoua), NOUN PAY (Bafoussam)",
    "parties": [
        ("Prologue", "Le 24 juin 2026", "P00"),
        ("Partie I", "Fondements", "C01–C02"),
        ("Partie II", "Le contexte international", "C03–C05"),
        ("Partie III", "Le contexte national", "C06–C07"),
        ("Partie IV", "Méthode : conduire l'audit", "C08–C12"),
        ("Partie V", "Pratique", "C13–C16"),
        ("Partie VI", "Défis avancés", "C17–C18"),
        ("Partie VII", "Recherche", "C19"),
    ],
    # jour : (thème court, contenu détaillé, ateliers, labs)
    "jours": {
        1: ('Ouverture · Le 24 juin 2026 · Données, traitements, acteurs', 'Présentation + P00 + C01', ['P00', 'C01'], []),
        2: ('Les principes du traitement', 'C02', ['C02'], ['LAB-01']),
        3: ("Sources internationales et africaines · Le RGPD hors d'Europe", 'C03 + C04', ['C03', 'C04'], []),
        4: ('Le NIST Privacy Framework et les normes ISO', 'C05', ['C05'], ['LAB-12']),
        5: ('La loi n° 2024/017 · La loi n° 2010/012 · Choisir ses critères', 'C06 + C07', ['C06', 'C07'], ['LAB-11']),
        6: ('Conduire un audit de protection des données', 'C08', ['C08'], []),
        7: ('Cartographier les traitements', 'C09', ['C09'], ['LAB-02']),
        8: ('Évaluer le risque pour les personnes', 'C10', ['C10'], ['LAB-03']),
        9: ('Auditer les droits des personnes', 'C11', ['C11'], ['LAB-04']),
        10: ('Auditer la sécurité des données', 'C12', ['C12'], ['LAB-05']),
        11: ('Sous-traitants · Transferts internationaux', 'C13 + C14', ['C13', 'C14'], ['LAB-06', 'LAB-07']),
        12: ('Les violations de données', 'C15', ['C15'], ['LAB-08']),
        13: ("Programme de conformité et rapport d'audit", 'C16', ['C16'], ['LAB-09']),
        14: ('Profilage, décisions automatisées et IA', 'C17', ['C17'], ['LAB-10']),
        15: ('Secteurs sensibles · Mesurer et articuler · Clôture', 'C18 + C19', ['C18', 'C19'], []),
    },
}

# dossier calculé depuis ce fichier, pour que la sortie soit la même sous Windows et sous Linux
import os as _os
APDC["dossier"] = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
ALL["APDC"] = APDC
