# Audit de Protection des Données et Conformité (APDC)

[← Tous les cours de MaletYon](https://github.com/maletyon) · [Livre (PDF)](APDC_main.pdf) · [Présentations](Présentation/) · [Fiches par chapitre](fiches/) · [Corrigés](correction/README.md)

**UE MSN-2S4-SEC02** · Master Professionnel en Sécurité des Systèmes Numériques · Semestre 4
Chaire UNESCO d'Afrique Centrale ACCES-TIC, sous la tutelle académique de l'École Nationale Supérieure Polytechnique de l'Université de Yaoundé I
Auteur : MINKA MI NGUIDJOÏ Thierry Emmanuel, enseignant-chercheur (LIMSI, ENSPY) · contact : maletyon@proton.me · année académique 2026-2027

> *Prouver la conformité, protéger les personnes : auditer l'application de la loi n° 2024/017.*

La loi n° 2024/017 du 23 décembre 2024 relative à la protection des données à caractère personnel s'applique pleinement depuis le 24 juin 2026, à l'expiration du délai de dix-huit mois de son article 73. Le cours apprend à auditer son application : recenser les traitements, apprécier le risque pour les personnes, vérifier sur pièces les principes, les droits, la sécurité, les sous-traitants, les transferts et la gestion des violations, puis conclure et faire corriger. Chaque exigence reçoit une cote OUI / NON / NEK ; l'état de conformité se mesure par μ, U et H, selon le programme de l'auditologie, et le cours distingue l'incertitude qui tient aux preuves de celle qui tient aux textes d'application encore attendus. Il s'appuie aussi sur la loi n° 2010/012, la Convention de Budapest, la Convention de Malabo et les normes ISO/IEC 29100, 27701, 29134 et 27018. Trois cas forment le fil rouge : NYANGA CRÉDIT (Bafoussam), le CENTRE MÉDICAL MBOLO (Bertoua) et NOUN PAY (Bafoussam).

## Ce que contient ce dépôt

| Élément | Où | Description |
|---|---|---|
| Le livre du cours | [`APDC_main.pdf`](APDC_main.pdf) | Traité complet (prologue, 16 chapitres, annexes), compilé depuis [`APDC_main.tex`](APDC_main.tex) |
| Les présentations | [`Présentation/`](Présentation/) | 16 présentations PowerPoint : vision d'ensemble et 15 séances de 2 heures, avec notes du présentateur |
| Les fiches d'exercices | [`fiches/`](fiches/) | 17 fiches de 40 questions au format texte, à distribuer en attendant l'ouverture de NDAP SUKULU |
| Le livret de correction | [`correction/`](correction/) | Accès réservé : voir la page du dossier |
| Les sources LaTeX | `front/`, `partie0/` à `partie6/`, `annexes/`, `bibliographie/`, `figures/`, [`Style_APDC.sty`](Style_APDC.sty) | Sources du livre |

## Organisation du cours (30 heures, 15 séances de 2 heures)

Les 30 heures sont consacrées au cours magistral. Les travaux dirigés (fiches, exercices de fin de chapitre) et les travaux pratiques (dix laboratoires) se font à la maison, sur NDAP SUKULU.

| Partie | Chapitres | Fichiers |
|---|---|---|
| **Prologue** | 0. Le 24 juin 2026 | [`partie0/`](partie0/) |
| **I. Fondements** | 1. Données, traitements, acteurs · 2. Les principes du traitement | [`partie1/`](partie1/) |
| **II. Méthode** | 3. Conduire un audit de protection des données · 4. Cartographier les traitements · 5. Évaluer le risque pour les personnes · 6. Auditer les droits des personnes · 7. Auditer la sécurité des données | [`partie2/`](partie2/) |
| **III. Cadre normatif, juridique et déontologique** | 8. La loi n° 2024/017 et le cadre africain · 9. Normes, certification et déontologie | [`partie3/`](partie3/) |
| **IV. Pratique** | 10. Sous-traitants et responsables conjoints · 11. Les transferts internationaux · 12. Les violations de données · 13. Programme de conformité et rapport d'audit | [`partie4/`](partie4/) |
| **V. Défis avancés** | 14. Profilage, décisions automatisées et intelligence artificielle · 15. Les secteurs sensibles | [`partie5/`](partie5/) |
| **VI. Recherche** | 16. Mesurer la conformité, articuler les normes | [`partie6/`](partie6/) |
| **Annexes** | A. Glossaire · B. Outils · C. Modèles de documents · D. Textes et normes · E. Bibliographie commentée · F. Contacts | [`annexes/`](annexes/) |

## NDAP SUKULU, la salle de classe compagnon

*Ndap sukulu* signifie « la salle de classe » en bassa, et *Malet Yon* « ton enseignant ». NDAP SUKULU est l'environnement d'évaluation du cours : une fiche de 20 questions tirées d'une banque de 100 par chapitre, et dix laboratoires pratiques, minutés et en nombre de tentatives limité. Le code de cours est **MSN-2S4-SEC02**. La présentation complète figure au début du livre.

| Utilisation | Où |
|---|---|
| En ligne | `https://maletyon.github.io/cours-apdc/ndap-sukulu/` |
| Sur un ordinateur, sans Internet | archive téléchargeable dans [`ndap-sukulu/`](ndap-sukulu/) |
| Sur un téléphone (fiches seulement) | `https://maletyon.github.io/cours-apdc/ndap-sukulu/telephone/` |
| Si votre réseau bloque `github.io` | adresse de secours `https://raw.githack.com/MaletYon/cours-apdc/main/ndap-sukulu/`, ou [archive à télécharger](https://github.com/MaletYon/cours-apdc/raw/main/ndap-sukulu/NDAP_SUKULU_APDC_ordinateur.zip) pour travailler hors ligne |

La connexion se fait avec le matricule et le mot de passe remis par l'enseignant. Les copies sont remises à l'enseignant sous forme d'un fichier chiffré ; il les corrige et publie les résultats, que chacun consulte dans l'application. Le mode d'emploi complet, pour l'étudiant et pour l'enseignant, est dans [`ndap-sukulu/README.md`](ndap-sukulu/README.md). Les fiches de 40 questions au format texte restent disponibles dans [`fiches/`](fiches/).

| Lab | Sujet | Chapitre |
|---|---|---|
| APDC-LAB-01 | Qualifier les données d'un export | 1, 2 |
| APDC-LAB-02 | Registre déclaré, fichiers découverts | 4 |
| APDC-LAB-03 | Évaluation d'impact de la téléconsultation | 5 |
| APDC-LAB-04 | Demandes des personnes et délais | 6 |
| APDC-LAB-05 | Journaux d'accès au dossier patient | 7 |
| APDC-LAB-06 | Contrats de sous-traitance | 10 |
| APDC-LAB-07 | Flux de données vers l'étranger | 11 |
| APDC-LAB-08 | Violation de données et notification | 12 |
| APDC-LAB-09 | Durées de conservation | 13 |
| APDC-LAB-10 | Audit intégrateur du profilage | 14, 16 |

## Sources de recherche

Le cours s'appuie sur deux prépublications de l'auteur, déposées sur HAL : *Vers l'auditologie* (`hal-05701007`) et *Modelling Epistemic Uncertainty in IS Audit* (`hal-05701270`). Le chapitre 16 présente, comme piste de recherche actuelle, un manuscrit en préparation de l'auteur et de ses coauteurs, Robert Thierry MASSOUSSI SONGO et Dieudonné BIALO, sur la loi n° 2024/017 et la chaîne pénale au Cameroun ; il n'est pas encore publié. Les autres travaux cités comme « en préparation » ne le sont pas non plus.

## Compiler le livre

Avec une distribution LaTeX : `pdflatex APDC_main`, `biber APDC_main`, `makeindex APDC_main`, puis deux fois `pdflatex APDC_main`.
Les présentations se régénèrent avec `python Présentation/_sources/run.py APDC all` (Python 3 et python-pptx).

## Textes, normes et documents sous licence

La loi n° 2024/017 est citée d'après le texte promulgué ; les articles reproduits dans le livre le sont textuellement. Les normes ISO et les autres documents sous licence cités dans le cours **ne sont pas fournis** dans ce dépôt. Les noms d'organisations, de personnes, les adresses et les montants des cas sont fictifs, et leurs dates sont antérieures à la rédaction du cours.

## Licence

Contenu pédagogique : [CC BY-NC-SA 4.0](LICENSE.md). Code du générateur de présentations : MIT. Voir [`LICENSE.md`](LICENSE.md).
