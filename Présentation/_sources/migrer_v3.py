# -*- coding: utf-8 -*-
"""Produit les spécifications des séances de la version 3 (19 chapitres) à
partir de celles de la version 1 (specs/APDC_v1) et de specs_v3_nouveaux.py."""
import io, re, pprint, copy, os
from specs_v3_nouveaux import J03, J04, J05_2010
V1='specs/APDC_v1'; V3='specs/APDC'
def old(n):
    g={}; exec(io.open('%s/J%02d.py'%(V1,n),encoding='utf-8').read(),g); return g['SPEC']
CH={1:1,2:2,3:8,4:9,5:10,6:11,7:12,8:6,9:5,10:13,11:14,12:15,13:16,14:17,15:18,16:19}
JR={1:1,2:2,3:6,4:7,5:8,6:9,7:10,10:11,11:11,12:12,13:13,14:14,15:15}
PA={'I':'I','II':'IV','III':'III','IV':'V','V':'VI','VI':'VII'}
TIT={1:"Ouverture · Le 24 juin 2026 · Données, traitements, acteurs",2:"Les principes du traitement",3:"Sources internationales et africaines · Le RGPD hors d'Europe",4:"Le NIST Privacy Framework et les normes ISO",5:"La loi n° 2024/017 · La loi n° 2010/012 · Choisir ses critères",6:"Conduire un audit de protection des données",7:"Cartographier les traitements",8:"Évaluer le risque pour les personnes",9:"Auditer les droits des personnes",10:"Auditer la sécurité des données",11:"Sous-traitants · Transferts internationaux",12:"Les violations de données",13:"Programme de conformité et rapport d'audit",14:"Profilage, décisions automatisées et IA",15:"Secteurs sensibles · Mesurer et articuler · Clôture"}
def walk(o,f):
    if isinstance(o,str): return f(o)
    if isinstance(o,list): return [walk(x,f) for x in o]
    if isinstance(o,tuple): return tuple(walk(x,f) for x in o)
    if isinstance(o,dict): return {k:walk(v,f) for k,v in o.items()}
    return o
def conv(own):
    def f(s):
        s=re.sub(r'\bC(\d\d)\b', lambda m:'C%02d'%CH.get(int(m.group(1)),int(m.group(1))), s)
        s=re.sub(r'([Cc]hapitres? )(\d+)\b', lambda m:m.group(1)+str(CH.get(int(m.group(2)),int(m.group(2)))), s)
        if own: s=re.sub(r'(?<![\d.,])%d\.(\d)(?!\d)'%own, lambda m:'%d.%s'%(CH[own],m.group(1)), s)
        s=re.sub(r'\b(Partie|PARTIE) (VI|IV|V|III|II|I)\b', lambda m:m.group(1)+' '+PA[m.group(2)], s)
        s=re.sub(r'\bJour (\d+)\b', lambda m:'Jour %d'%JR.get(int(m.group(1)),int(m.group(1))), s)
        return s
    return f
def ecrire(d,spec):
    for x in spec:
        if x.get('k')=='title': x['tag']="Jour %d / 15 · Séance de 2 heures"%d
        if x.get('k')=='fin' and d<15: x['next']="Jour %d · %s"%(d+1,TIT[d+1])
    io.open('%s/J%02d.py'%(V3,d),'w',encoding='utf-8').write("SPEC = "+pprint.pformat(spec,width=220,sort_dicts=False)+"\n")
def rappel(spec,d,items):
    for x in spec:
        if x.get('k')=='synthese' and 'Rappel' in x.get('title',''):
            x['kicker']="Jour %d · %s"%(d-1,TIT[d-1])
            if items: x['items']=items
            return
def fin_items(spec,items):
    for x in spec:
        if x.get('k')=='fin': x['items']=items
# J01, J02
s=walk(old(1),conv(1)); ecrire(1,s)
s=walk(old(2),conv(2)); fin_items(s,["La filiation des principes, de l'OCDE à la loi","Le statut de chaque instrument","L'article 3 du RGPD"]); ecrire(2,s)
ecrire(3,copy.deepcopy(J03)); ecrire(4,copy.deepcopy(J04))
# J05 : ancien J08 allégé + loi de 2010
o=walk(old(8),conv(8))
garde=[x for x in o if not (x.get('k')=='compare' or (x.get('k')=='cards' and 'africain' in x.get('title','')))]
for x in garde:
    if x.get('k')=='title': x.update(title="La loi n° 2024/017\nLa loi n° 2010/012", right="Partie III · Chapitres C06 et C07", sub="« Une loi nouvelle n'efface pas les anciennes. Elle oblige à les relire. » Principe du cours")
    if x.get('k')=='agenda': x['items']=[("10 min","**Ce que la loi a internalisé**, ce qu'elle a ajouté"),("20 min","**Autorisation préalable** et textes d'application attendus"),("15 min","**L'Autorité** et les **sanctions**"),("25 min","**La loi n° 2010/012** : sécurité, conservation, vie privée, délits"),("20 min","**Choisir ses critères** · la carte d'applicabilité"),("30 min","**Exercice** en séance · synthèse")]
    if x.get('k')=='chapitre': x.update(part="PARTIE III · LE CONTEXTE NATIONAL", title="La loi n° 2024/017 : autorisation, Autorité, sanctions", question="« Une autorisation pour chaque traitement. Très bien. Où dépose-t-on la demande ? »")
    if x.get('k')=='objectifs': x['items']=["Dire ce que la loi a **internalisé** et ce qu'elle a **ajouté**","Expliquer le **régime d'autorisation préalable** tant que l'Autorité n'est pas organisée","Décrire l'échelle des **sanctions**","Présenter ce que la **loi n° 2010/012** impose encore","Dresser une **carte d'applicabilité**"]
rappel(garde,5,["Une loi **oblige**, une norme **se certifie**, un cadre volontaire **se déclare**","Le noyau du NIST compte **cinq fonctions**","L'ISO/IEC 27701 est **autonome** depuis 2025","Autorisation préalable et rapport annuel n'ont **aucun équivalent** étranger"])
i=[k for k,x in enumerate(garde) if x.get('k')=='exercice'][0]
spec=garde[:i]+copy.deepcopy(J05_2010)+garde[i:]
for x in spec:
    if x.get('k')=='synthese' and 'Rappel' not in x.get('title',''): x['items']=["La loi **internalise** les principes internationaux et y ajoute l'autorisation préalable","**Tout** traitement est soumis à autorisation (article 19)","La loi n° **2010/012** subsiste pour ce qui n'est pas contraire","Dix ans de conservation : établir d'abord **à qui** l'obligation s'applique","Critères : **obligatoire, étranger opposable, contractuel, volontaire déclaré**"]
    if x.get('k')=='maison': x['lecture']=["Chapitres C06 et C07 en entier","Exercices 6.4 (le tableau des textes attendus) et 7.4 (dix ans ou le nécessaire)"]
fin_items(spec,["Mandat, critères, périmètre","La force des preuves","Coter OUI, NON, NEK et conclure"]); ecrire(5,spec)
# J06 à J10 : anciens J03 à J07
for o_,n in ((3,6),(4,7),(5,8),(6,9),(7,10)):
    s=walk(old(o_),conv(o_))
    if n==6: rappel(s,6,["La loi **internalise** les principes internationaux","**Tout** traitement est soumis à autorisation préalable","La loi n° **2010/012** reste applicable","Les critères se choisissent dans une **carte d'applicabilité**"])
    else: rappel(s,n,None)
    if n==10: fin_items(s,["Le contrat de sous-traitance et ses douze clauses","Qu'est-ce qu'un transfert","Les quatre vérifications de l'article 32"])
    ecrire(n,s)
# J11 : anciens J10 et J11 fusionnés
a=walk(old(10),conv(10)); b=walk(old(11),conv(11))
def corps(sp,avec_exo):
    out=[]; ok=False
    for x in sp:
        if x.get('k')=='chapitre': ok=True
        if x.get('k')=='exercice' and not avec_exo: continue
        if x.get('k') in ('synthese','maison','fin') and ok: 
            if x.get('k')=='synthese' and 'Rappel' in x.get('title',''): continue
            break
        if ok: out.append(x)
    return out
def un(sp,k,rap=False): return [x for x in sp if x.get('k')==k and (('Rappel' in x.get('title',''))==rap)][0]
t=copy.deepcopy(un(a,'title')); t.update(title="Sous-traitants\net transferts internationaux", right="Partie V · Chapitres C13 et C14")
r=copy.deepcopy(un(walk(old(8),conv(8)),'synthese',True)); r['kicker']="Jour 10 · "+TIT[10]
ag={"k":"agenda","items":[("15 min","**Les obligations** de la loi envers les sous-traitants"),("20 min","**Le contrat** et ses douze clauses · vérifier l'exécution"),("10 min","**Les responsables conjoints**"),("15 min","**Qu'est-ce qu'un transfert** · l'article 32"),("20 min","**Cartographier les flux sortants** · coter sans liste ni clauses"),("40 min","**Exercice** en séance · synthèse")]}
sa=un(a,'synthese'); sb=un(b,'synthese'); sy={"k":"synthese","items":sa['items'][:3]+sb['items'][:3]}
ma={"k":"maison","lecture":["Chapitres C13 et C14 en entier"]+[l for l in un(a,'maison').get('lecture',[])[1:]]+[l for l in un(b,'maison').get('lecture',[])[1:]]}
for k in ('ateliers','labs'):
    v=un(a,'maison').get(k); w=un(b,'maison').get(k)
    if v or w: ma[k]=(v or [])+(w or []) if isinstance(v or w,list) else (v or w)
spec=[t,r,ag]+corps(a,False)+corps(b,True)+[sy,ma,un(b,'fin')]
ecrire(11,spec)
for d in (12,13,14,15):
    s=walk(old(d),conv(d)); rappel(s,d,None); ecrire(d,s)
# vision globale et métadonnées
j=io.open(V1+'/J00.py',encoding='utf-8').read()
j=j.replace("un prologue, six parties, seize chapitres","un prologue, sept parties, dix-neuf chapitres").replace("Un prologue, six parties, seize chapitres","Un prologue, sept parties, dix-neuf chapitres").replace("du prologue à la Partie VI","du prologue à la Partie VII")
a_=j.index('        ["Partie I", "Fondements'); b_=j.index(']',j.index('["Partie VI", "Recherche'))+1
j=j[:a_]+'''        ["Partie I", "Fondements : données, acteurs, principes", "C01 à C02", "J01 à J02"],
        ["Partie II", "Contexte international : sources, RGPD, NIST et ISO", "C03 à C05", "J03 à J04"],
        ["Partie III", "Contexte national : loi de 2024, loi de 2010, critères", "C06 à C07", "J05"],
        ["Partie IV", "Méthode : audit, registre, risque, droits, sécurité", "C08 à C12", "J06 à J10"],
        ["Partie V", "Sous-traitants, transferts, violations, rapport", "C13 à C16", "J11 à J13"],
        ["Partie VI", "Profilage et IA, secteurs sensibles", "C17 à C18", "J14 à J15"],
        ["Partie VII", "Recherche : mesurer, articuler", "C19", "J15"]'''+j[b_:]
CONT={1:"P00 + C01",2:"C02",3:"C03 + C04",4:"C05",5:"C06 + C07",6:"C08",7:"C09",8:"C10",9:"C11",10:"C12",11:"C13 + C14",12:"C15",13:"C16",14:"C17",15:"C18 + C19"}
paires=['["J01 · J02", "P00, C01 · C02", "aucun · LAB-01"]','["J03 · J04", "C03, C04 · C05", "aucun · aucun"]','["J05 · J06", "C06, C07 · C08", "aucun · aucun"]','["J07 · J08", "C09 · C10", "LAB-02 · LAB-03"]','["J09 · J10", "C11 · C12", "LAB-04 · LAB-05"]','["J11 · J12", "C13, C14 · C15", "LAB-06, LAB-07 · LAB-08"]','["J13 · J14", "C16 · C17", "LAB-09 · LAB-10"]','["J15", "C18, C19", "aucun"]']
a_=j.index('["J01 · J02"'); b_=j.index(']',j.index('["J15", "C15, C16"'))+1
j=j[:a_]+(',\n        '.join(paires))+j[b_:]
for d in range(1,16):
    j=re.sub(r'\["J%02d", "[^"]*", "[^"]*"\]'%d, lambda m:'["J%02d", "%s", "%s"]'%(d,TIT[d],CONT[d]), j, count=1)
for o_,n in (("C14, C16","C17, C19"),('"C13"]','"C16"]'),('"C12"]','"C15"]'),('"C11"]','"C14"]'),('"C10"]','"C13"]'),('"C07"]','"C12"]'),('"C06"]','"C11"]'),('"C05"]','"C10"]'),('"C04"]','"C09"]')):
    a_=j.index('"k": "table", "title": "Les dix labs'); j=j[:a_]+j[a_:].replace(o_,n,1)
io.open(V3+'/J00.py','w',encoding='utf-8').write(j)
c=io.open('courses.py',encoding='utf-8').read()
a_=c.index('APDC = {'); p1=c.index('"parties": [',a_); p2=c.index('    },\n}',p1)+len('    },\n}')
bloc='''"parties": [
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
'''
LAB={2:["LAB-01"],7:["LAB-02"],8:["LAB-03"],9:["LAB-04"],10:["LAB-05"],11:["LAB-06","LAB-07"],12:["LAB-08"],13:["LAB-09"],14:["LAB-10"]}
for d in range(1,16):
    at=re.findall(r'[PC]\d\d',CONT[d]); bloc+='        %d: (%r, %r, %r, %r),\n'%(d,TIT[d],("Présentation + " if d==1 else "")+CONT[d],at,LAB.get(d,[]))
bloc+='    },\n}'
if 'Partie VII' not in c[a_:p2]: c=c[:p1]+bloc+c[p2:]
io.open('courses.py','w',encoding='utf-8').write(c)
print('ok', sorted(os.listdir(V3)))
