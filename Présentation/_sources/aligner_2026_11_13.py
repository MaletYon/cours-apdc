# Alignement des présentations APDC sur les retouches du livre du 13 novembre 2026
# et sur les labs 11 et 12. À lancer une seule fois depuis le dossier _sources.
import importlib.util,pprint
D='specs/APDC/'
def L(n):
    s=importlib.util.spec_from_file_location('m',D+n+'.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m.SPEC
def W(n,S):
    open(D+n+'.py','w',encoding='utf-8').write('SPEC = '+pprint.pformat(S,width=240,sort_dicts=False)+'\n')
def idx(S,title):
    for i,d in enumerate(S):
        if d.get('title')==title: return i
    raise KeyError(title)
def syn(S):
    return [d for d in S if d['k']=='synthese' and 'title' not in d][0]

# J01
S=L('J01'); i=idx(S,'Les acteurs du traitement')
S.insert(i+1,{'k':'table','title':'Les acteurs dans quatre vocabulaires','kicker':'Tableau 1.1',
 'head':['Loi n° 2024/017','ISO/IEC 29100','RGPD (UE)','NIST Privacy Framework'],'widths':[2.9,2.9,2.7,3.3],'size':12,
 'rows':[['Personne concernée','PII principal','Personne concernée','Individu'],
         ['Responsable du traitement','PII controller','Responsable du traitement','Organisation, décrite par son rôle'],
         ['Sous-traitant','PII processor','Sous-traitant','Organisation, même remarque'],
         ['Destinataire, tiers','Tiers','Destinataire, tiers',"Autres acteurs de l'écosystème"],
         ['Autorité de protection','Autorité de contrôle (hors norme)','Autorité de contrôle','Hors cadre']],
 'note':"Le cadre du NIST est **volontaire** : il ne fixe aucune qualité juridique et parle d'une organisation et de son rôle."})
W('J01',S)

# J08
S=L('J08'); i=idx(S,"Les étapes d'une évaluation d'impact")
S.insert(i+1,{'k':'compare','title':"Le risque de vie privée selon le NIST et l'ISO",'kicker':'Deux référentiels volontaires',
 'left':{'head':'NIST · les actions problématiques','items':["Une opération peut **nuire** alors que le système fonctionne comme prévu","Trois objectifs : **prévisibilité, maîtrise, dissociabilité**","Ils complètent confidentialité, intégrité, disponibilité"]},
 'right':{'head':'ISO/IEC 27557:2022','items':["La démarche de l'**ISO 31000** appliquée à la vie privée","Deux lectures tenues ensemble : la **personne**, puis l'**organisation**"]},
 'bottom':"Ni l'un ni l'autre n'est un critère de conformité au Cameroun : l'auditeur s'en sert pour ne rien oublier et le **déclare dans son plan**."})
W('J08',S)

# J09
S=L('J09'); i=idx(S,'Le délai, un critère à déclarer')
S.insert(i+1,{'k':'points','title':"D'où viennent les trente jours",'kicker':'La source du critère de substitution',
 'items':["Le plan d'audit donne la **source** du critère","Le RGPD, article 12, paragraphe 3 : réponse dans **un mois**, prolongeable de deux mois pour les demandes complexes ou nombreuses","KORO AUDIT l'a converti en **trente jours calendaires** pour le mesurer sans ambiguïté","Le règlement ne s'applique pas à NYANGA : il est **emprunté et déclaré** comme tel","Pour NOUN DIASPORA, soumise aux deux textes, le mois redevient une **obligation**"]})
W('J09',S)

# J10
S=L('J10'); i=idx(S,'Dix obligations, dix contrôles'); t=S[i]
t['head']=['Obligation','NIST Protect-P',"Contrôle d'audit"]; t['widths']=[4.2,2.2,5.2]; t['size']=12
pp={'Disponibilité et résilience':'PR.PT-P','Contrôle des accès':'PR.AC-P','Traçabilité a posteriori':'PR.PT-P','Protection des supports':'PR.PT-P, PR.DS-P','Sauvegardes':'PR.PO-P','Vérification des destinataires':'PR.AC-P','Rapport annuel (alinéa 2)':'Sans objet'}
t['rows']=[[r[0],pp[r[0]],r[1]] for r in t['rows']]
t['note']="Correspondances **indicatives** avec le cadre du NIST ; la sécurité figure aussi aux articles **7, 15, 22, 24 et 25**."
S.insert(i+1,{'k':'compare','title':'Un second texte, une durée à déclarer','kicker':'Loi n° 2010/012 · journal des consultations',
 'left':{'head':"La loi de 2010 s'ajoute",'items':["Son **article 26** demande aux exploitants de protéger leurs systèmes","Ses articles 41 à 48 protègent la vie privée dans les communications","Un **compte partagé** peut fonder un écart aux deux lois"]},
 'right':{'head':'Combien de temps garder le journal','items':["L'article 27 dit « a posteriori », sans durée","Les dix ans de l'article 29 visent les données de connexion et de trafic","Critère du cours : **un an au moins**, déclaré au plan"]},
 'bottom':"Le rapport écrit « un an (critère de l'audit) » et non « un an (durée légale) ». Le journal est lui-même un fichier de données personnelles."})
j=idx(S,'Le domaine D3 à MBOLO')
S.insert(j+1,{'k':'table','title':'Le domaine D3 à NYANGA','kicker':'Septembre 2026 · µ 0,50 · U 0,125 · H 1,41','head':['Exigence','Cote','Preuve'],'widths':[6.4,1.4,3.8],'size':12,
 'rows':[["L'équipement à l'origine de l'incident est remplacé et tenu à jour",'OUI','Bon de livraison, correctifs'],
         ['Un inventaire des équipements est tenu','OUI','Inventaire de mars 2026'],
         ['Les journaux sont centralisés et conservés','OUI','Treize mois en ligne'],
         ['Les sauvegardes sont restaurables','OUI','Test du 3 septembre'],
         ["Chaque agent n'accède qu'aux clients de son agence",'NON',"Six comptes d'agence testés"],
         ['Les relevés sont transmis par un canal maîtrisé','NON','Messagerie personnelle'],
         ['Les habilitations sont revues','NON','Aucune revue depuis 2023'],
         ["Les mesures suivent le référentiel de l'Autorité (art. 24)",'NEK','Référentiel non publié']],
 'note':"Seul domaine **clair** de la mission, et pourtant non conforme : les trois NON portent sur la **limitation des accès**."})
syn(S)['items'].append("À NYANGA, D3 est le seul domaine **clair** : quatre OUI, trois NON, un NEK de critère")
W('J10',S)

# J11
S=L('J11'); i=idx(S,'Cinq contrats')
S.insert(i+1,{'k':'points','title':'Quand le sous-traitant est européen','kicker':"L'hébergeur de NOUN PAY · article 28 du RGPD",
 'items':["Établi dans l'Union, l'hébergeur est soumis au **RGPD** quel que soit le pays de son client","L'article 28 lui impose instruction documentée, confidentialité, autorisation des sous-traitants ultérieurs, aide aux demandes, **audits**","Son contrat contient déjà la plupart des douze clauses : on le vérifie **clause par clause**","Écrit pour le droit européen, il ne cite ni l'**article 30** ni l'Autorité camerounaise : l'écart se note","Le client reste **responsable** au titre de l'article 20"]})
i=idx(S,'La grille des transferts de NOUN PAY')
S.insert(i+1,{'k':'compare','title':"Les données qui reviennent de l'Union européenne",'kicker':'NOUN DIASPORA · 6 840 clients en France et en Belgique',
 'left':{'head':'Au titre de la loi camerounaise','items':["Le traitement à Douala de données venues de l'étranger reste soumis à l'**article 19**"]},
 'right':{'head':'Au titre du RGPD, chapitre V','items':["La consultation depuis Douala est un **transfert vers un pays tiers**","Pas de décision d'adéquation : **clauses contractuelles types** de 2021 et évaluation du droit local","Aucune clause signée à NOUN PAY : **NON**"]},
 'bottom':"Un même flux, **deux exigences** cotées séparément. Les fiches pays du chapitre 3 (Maroc, Côte d'Ivoire) informent le rapport sans lever le NEK de critère."})
syn(S)['items'][-1]="Sans liste ni clauses types : **NEK de critère** ; un flux venu de l'Union se cote **deux fois**"
W('J11',S)

# J12
S=L('J12'); i=idx(S,'Informer pendant une enquête pénale')
S.insert(i+1,{'k':'table','title':'La même violation sous deux textes','kicker':'Tableau 15.2 · une organisation exposée au RGPD',
 'head':['Question','Loi n° 2024/017, art. 22','RGPD, art. 33 et 34'],'widths':[2.8,4.4,4.4],'size':13,
 'rows':[['Quelles violations','Toutes','Celles qui présentent un risque'],
         ['Qui informer',"L'Autorité et la personne","L'autorité ; la personne si le risque est élevé"],
         ['Dans quel délai','« Sans délai », non chiffré',"72 heures pour l'autorité"],
         ['Cote du délai','Temps mesuré, rapproché des raisons du retard',"OUI ou NON sur l'horodatage"]],
 'note':"Deux cotes, jamais fondues. Règle pratique : la **plus exigeante** des deux réponses, informer **toutes** les personnes et tenir les **72 heures**."})
syn(S)['items'].insert(2,"Exposée au RGPD, l'organisation suit **deux horloges** et porte deux cotes")
W('J12',S)

# J13
S=L('J13'); i=idx(S,'La synthèse des six domaines')
S[i]['note']="**28 écarts** établis, **10 NEK** dont six de critère, **8 exigences** qui fonctionnent. Les 46 exigences figurent à l'**Annexe G**."
S.insert(i,{'k':'table','title':'Le domaine D6, gouvernance, à NYANGA','kicker':'µ 0 · U 0,25 · H 0,81','head':['Exigence','Cote','Preuve'],'widths':[6.6,1.4,3.6],'size':13,
 'rows':[['Le risque de chaque traitement est évalué (art. 25)','NON','Aucune évaluation'],
         ["Une évaluation d'impact précède les traitements à risque élevé (art. 33)",'NON','Douze traitements, aucune'],
         ['Un dossier de conformité peut être présenté au contrôle (art. 35)','NON','Pièces dispersées'],
         ["Le rapport annuel est adressé à l'Autorité (art. 27(2))",'NEK','Autorité non organisée']],
 'note':"L'absence de toute évaluation se constate sans le texte d'application : **NON** et non NEK. Ce domaine explique les cinq autres."})
i=idx(S,'La synthèse des six domaines')
S.insert(i+1,{'k':'points','title':'Une limite du plan, dite dans le rapport','kicker':'Le transfert vers Abidjan',
 'items':["Les huit exigences de D4 portent sur les **contrats** ; le transfert vers Abidjan n'y était pas isolé","Le rapport le signale et le cote **hors décompte**","« Le transfert est autorisé » : **NON**, faute d'autorisation","« Le pays offre un niveau suffisant » : **NEK de critère**, faute de liste","Une exigence oubliée ne modifie pas le décompte après coup : elle s'écrit, se cote à part et entre au **plan suivant**"]})
W('J13',S)

# J14
S=L('J14'); i=idx(S,'NOUN SCORE, octobre 2026')
S.insert(i+1,{'k':'table','title':"Trois textes sur l'intelligence artificielle",'kicker':"Tableau 17.2 · aucun n'est un critère obligatoire au Cameroun",
 'head':['Texte','Nature',"Ce que l'auditeur en retient"],'widths':[3.4,2.6,5.6],'size':12,
 'rows':[['NIST AI RMF 1.0 (2023)','Cadre volontaire','Gouverner, cartographier, mesurer, gérer ; équité, explicabilité, vie privée'],
         ['Règlement (UE) 2024/1689',"Obligatoire dans l'Union",'Approche par niveau de risque ; la notation de solvabilité est à **haut risque**'],
         ["Stratégie continentale de l'Union africaine (2024)",'Orientation politique','Appel à des cadres nationaux et à la protection des données']],
 'note':"Un texte étranger se cite **pour ce qu'il est** : emprunté et déclaré, il ne fonde aucune non-conformité légale."})
S.insert(i+2,{'k':'points','title':'Quatre questions pour un système qui apprend','kicker':'Sans réponse : NEK de preuve',
 'items':["**Les données d'entraînement** : d'où viennent-elles, les personnes sont-elles informées (articles 9, 11, 21) ?","**La dérive** : qui vérifie que les résultats ne changent pas en silence ?","**L'explication** : sait-on dire à une personne pourquoi elle a été refusée (article 44) ?","**Le fournisseur** : que dit le contrat sur la réutilisation des données (articles 30, 32) ?","Le NEK se lève par des pièces : **fiche du modèle, journal des réentraînements, contrat**"]})
syn(S)['items'].insert(4,"NIST AI RMF, règlement européen, stratégie africaine : des références **déclarées**, pas des critères obligatoires")
W('J14',S)

# J15
S=L('J15'); i=idx(S,'Les règles propres à chaque secteur')
S.insert(i+1,{'k':'table','title':"Les données d'un opérateur et leurs textes",'kicker':'Tableau 18.2 · les télécommunications',
 'head':['Donnée','Texte particulier',"Question d'audit"],'widths':[2.8,4.2,4.6],'size':12,
 'rows':[["Identité de l'abonné",'Décret n° 2015/3759 du 3 septembre 2015','Quelles pièces sont copiées, où, qui y accède en point de vente ?'],
         ['Contenu des communications','Loi n° 2010/012, articles 41 à 48',"Le secret est-il garanti, y compris envers les salariés ?"],
         ['Connexion et trafic','Loi n° 2010/012, article 29','Quelle durée, qui peut interroger ces données ?'],
         ["Droits de l'utilisateur",'Directive n° 07/08-UEAC-133-CM-18 (CEMAC)',"L'abonné est-il informé, peut-il s'opposer à la prospection ?"]],
 'note':"L'opérateur est **sous-traitant** pour les SMS de ses clients et **responsable** pour l'acheminement et le trafic qu'il conserve."})
i=idx(S,'Une piste de recherche actuelle')
S[i]['items'].append("Une quatrième zone **proposée par ce cours** : **T4 conservation**, durée limitée (articles 13 et 28) face aux dix ans d'autres textes ; elle n'engage pas les coauteurs")
f=[d for d in S if d['k']=='fin'][0]
f['items']=['Refaire les douze labs de NDAP SUKULU','Relire les synthèses des dix-neuf chapitres','Préparer une question de recherche']
W('J15',S)

# J00
p=D+'J00.py'; j=open(p,encoding='utf-8').read()
def R(a,b):
    global j
    assert a in j,a
    j=j.replace(a,b,1)
R('("10", "labs pratiques','("12", "labs pratiques')
R('["J03 · J04", "C03, C04 · C05", "aucun · aucun"]','["J03 · J04", "C03, C04 · C05", "aucun · LAB-12"]')
R('["J05 · J06", "C06, C07 · C08", "aucun · aucun"]','["J05 · J06", "C06, C07 · C08", "LAB-11 · aucun"]')
R('"title": "Les dix labs de NDAP SUKULU"','"title": "Les douze labs de NDAP SUKULU"')
R('"head": ["Lab", "Intitulé", "Chapitre"], "widths": [1.6, 7.8, 2], "rows": [','"head": ["Lab", "Intitulé", "Chapitre"], "widths": [1.6, 7.8, 2], "size": 11, "rows": [')
R('        ["LAB-10", "Audit intégrateur du profilage", "C17, C19"],\n','        ["LAB-10", "Audit intégrateur du profilage", "C17, C19"],\n        ["LAB-11", "La loi de 2010 à NYANGA", "C07"],\n        ["LAB-12", "Double cote et profil NIST à NOUN PAY", "C04, C05"],\n')
open(p,'w',encoding='utf-8').write(j)

c=open('courses.py',encoding='utf-8').read()
a="4: ('Le NIST Privacy Framework et les normes ISO', 'C05', ['C05'], []),"; assert a in c; c=c.replace(a,a.replace("[]),","['LAB-12']),"))
a="5: ('La loi n° 2024/017 · La loi n° 2010/012 · Choisir ses critères', 'C06 + C07', ['C06', 'C07'], []),"; assert a in c; c=c.replace(a,a.replace("[]),","['LAB-11']),"))
open('courses.py','w',encoding='utf-8').write(c)
r=open('run.py',encoding='utf-8').read()
a='    "LAB-10": "Audit intégrateur du profilage",\n'; assert a in r
r=r.replace(a,a+'    "LAB-11": "La loi de 2010 à NYANGA",\n    "LAB-12": "Double cote et profil NIST à NOUN PAY",\n')
open('run.py','w',encoding='utf-8').write(r)
print('ok')
