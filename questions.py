import pdfextract.pdfextract as pdfx
import json

mainfile = '/tmp/myfile.pdf'

questiongroups = \
[ \
{ "group":"Primo gruppo", "questions" : [ \
{ "id":1, "text":"Misure ed errori (definizione, scrittura, combinazione e propagazione nei calcoli)", "pages":[11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25,27,28] }, \
{ "id":2, "text":"Vettori: definizione, prodotto per scalari, somma, prodotto scalare", "pages":[31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49] }, \
{ "id":3, "text":"Vettori: prodotto vettoriale e proprietà, prodotto misto, momento di un vettore, coppie di vettori", "pages":[50,51,53,53,54,55,56,57] }, \
{ "id":4, "text":"Ascissa curvilinea, equazioni della traiettoria, legge oraria, velocità, accelerazione, raggio di curvatura", "pages":[58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79] }, \
{ "id":5, "text":"Moto rettilineo uniforme e uniformemente accelerato", "pages":[80,81,82,83,84,85,86,87,88] }, \
{ "id":6, "text":"Moto del proiettile", "pages":[89,90,91,81,82,83,85,86,87,88] }, \
{ "id":7, "text":"Moto circolare uniforme e uniformemente accelerato", "pages":[92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107] }, \
{ "id":8, "text":"Moto armonico", "pages":[108,109,110,111,112,113,114,115,116,117] }, \
{ "id":9, "text":"Moti relativi", "pages":[118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140] } \
]}, \
\
{ "group":"Secondo gruppo", "questions" : [ \
{ "id":10, "text":"Forza peso (moto, lavoro ed energia potenziale)", "pages":[153,154,155,156,145,146,147,148,545,85,86,87,88,201,203,206] }, \
{ "id":11, "text":"Forza elastica e legge di Hooke (moto, lavoro ed energia potenziale)", "pages":[157,158,159,160,161,162,163,164,201,202,204,205] }, \
{ "id":12, "text":"Resistenza di fluidi in regime viscoso e turbolento", "pages":[170,171,172,173,174,274,275,276,277,278,410,411,414] }, \
{ "id":13, "text":"Attrito statico, dinamico, volvente", "pages":[217,218,219,220,221,272,273] }, \
{ "id":14, "text":"Oscillatore armonico libero (con dimostrazioni) e smorzato senza forzante (senza dimostrazioni)", "pages":[162,163,164,222,223,224,225,226,227,228,229,230,231] }, \
{ "id":15, "text":"Oscillatore armonico libero e smorzato con forzante sinusoidale, risonanza, fase", "pages":[165,166,167,168,169,232,233,234,235,236,237] }, \
{ "id":16, "text":"Lavoro di forze conservative ed energia potenziale", "pages":[183,184,185,186,187,191,195,196,197,198,199,200,201,202,203,204,205,206,207,208] }, \
{ "id":17, "text":"Teorema delle forze vive", "pages":[193,194,183,184,185,186,187] }, \
{ "id":18, "text":"Energia meccanica", "pages":[197,198,193,194,183,184,185,186,187] }, \
{ "id":19, "text":"Pendolo semplice", "pages":[212,213,214,215,216,545,162,163,164] }, \
{ "id":20, "text":"Equazioni cardinali della dinamica dei sistemi di punti materiali", "pages":[238,239,240,241,242,243,244,245,246,247,248,249,250,251] }, \
{ "id":21, "text":"Teoremi di König del momento angolare e dell'energia cinetica", "pages":[244,252,253,256,545,238,239,240,241,242,243] }, \
{ "id":22, "text":"Forze centrali (definizione, energia, moto, momento angolare)", "pages":[209,210,211,545,195,196,199,200] }, \
{ "id":23, "text":"Moto del razzo", "pages":[248,545,239,240,241,242,243] }, \
{ "id":24, "text":"Corpi rigidi: definizione, gradi di libertà, atto di moto rototraslatorio", "pages":[257,258,259,260,261,262,263,264,265,266,267,271,545,238,239,240,241,242,243,244,245,246,247,248,249,250,251] }, \
{ "id":25, "text":"Corpi rigidi: momento d'inerzia, lavoro delle forze esterne, energia", "pages":[263,264,265,266,267,270,271,545,238,239,240,241,242,243,244,245,246,247,248,249,250,251,257,258,259,260,261,262] }, \
{ "id":26, "text":"Urti: elastici, anelastici", "pages":[279,280,281,282,283,284,285,286,287,288,289,290,293,294,299,300,545,291,292,295,296,297,298,301] }, \
{ "id":27, "text":"Onde meccaniche: modello di corda vibrante o di catena di molle (a scelta dello studente)", "pages":[302,303,304,305,306,307,308,309,310,311,312,313] }, \
{ "id":28, "text":"Onde meccaniche: pacchetto d’onda, energia di un’onda, fronti d’onda piani o sferici", "pages":[325,326,327,328,329,330,331,332,333,334,335,336,337,338,545,302,303,304,305,306,307,308,309,310,311,312,313] }, \
{ "id":29, "text":"Onde acustiche: velocità del suono, valutazione del volume in dB, modello psicoacustico (qualitativamente), massimo volume in atmosfera", "pages":[339,340,341,342,343,344,545,325,326,327,328,329,330,331,332,333,334,335,336] }, \
{ "id":30, "text":"Definizione della forza gravitazionale ed esperienza di Cavendish", "pages":[345,346,347,348,349,350,351,352] }, \
{ "id":31, "text":"Teorema di Gauss per il campo gravitazionale", "pages":[353,354,355,356,357,545,346,347,348,349,350,351,352] }, \
{ "id":32, "text":"Campo gravitazionale in una sfera cava e in una sfera di densità uniforme, modello del campo gravitazionale terrestre (qualitativamente)", "pages":[358,359,360,361,362,545,353,354,355,356,357] }, \
{ "id":33, "text":"Energia di un corpo in un campo gravitazionale e traiettorie, velocità di fuga, orbita geostazionaria", "pages":[363,364,365,366,367,368,545,346,347,348,349,350,351,352] }, \
{ "id":34, "text":"Leggi di Keplero", "pages":[369,370,371,545,363,364,365,366,367,368] }, \
{ "id":35, "text":"Statica dei liquidi (dimostrazione del principio di Archimede, Stevin, Pascal)", "pages":[372,373,374,375,376,377,378,379,380,381,382,383,384,385] }, \
{ "id":36, "text":"Vasi comunicanti, leva idraulica, barometro di Torricelli", "pages":[386,387,388,545,372,373,374,375,376,377,378,379,380,381,382,383,384,385] }, \
{ "id":37, "text":"Andamento della pressione in atmosfera ed altezza di scala", "pages":[389,390,545,372,373,374,375,376,377,378,379,380,381,382,383,384,385] }, \
{ "id":38, "text":"Equazione di continuità in forma integrale e differenziale", "pages":[391,392,393,394,395,396,397] }, \
{ "id":39, "text":"Derivata sostanziale e struttura delle equazioni della dinamica dei fluidi", "pages": [398,399,400,401,402,403,404,545,391,392,393,394,395,396,397] }, \
{ "id":40, "text":"Teorema di Bernoulli", "pages":[405,406,407,408] }, \
{ "id":41, "text":"Effetto Venturi e tubi di Pitot", "pages":[409,412,545,391,392,393,394,395,396,397,405,406,407,408] }, \
{ "id":42, "text":"Moto di Poiseuille in un tubo e moto turbolento (qualitativamente)", "pages":[414,415,416,417,418,419,545,391,392,393,394,395,396,397] } \
]}, \
\
{ "group":"Terzo gruppo", "questions" : [ \
{ "id":43, "text":"Principio Zero della Termodinamica e definizione empirica della temperatura", "pages":[434,435,436,437,438,439,440,545,423,424,425,426,427,428,429,430,431,432,433] }, \
{ "id":44, "text":"Solidi, liquidi, Gas ideali: equazioni di stato e trasformazioni", "pages":[447,448,449,450,451,452,453,454,455,456,457,545,441,442,443,444,445,446] }, \
{ "id":45, "text":"Primo Principio della Termodinamica e applicazioni al calcolo del lavoro e calore nelle trasformazioni dei gas ideali", "pages":[441,442,443,444,445,446,453,454,457,545,447,448,449,450,451,452,455,456] }, \
{ "id":46, "text":"Teoria cinetica dei gas ideali ed equazione di van der Waals per gas reali", "pages":[458,459,460,461,462,463,464,465,466,467,468,469,470,545,294,295] }, \
{ "id":47, "text":"Entalpia: definizione, proprietà ed applicazione ai sistemi aperti", "pages":[471,472,473,474,475,476,477,545,442,443,444,445,446,447] }, \
{ "id":48, "text":"Cicli termodinamici: Otto/Beau de Rochas, Diesel, Brayton-Joule, Rankine", "pages":[479,480,481,482,483,523,524,525,526,545,484,485,500,501] }, \
{ "id":49, "text":"Ciclo di Carnot: definizione, calcolo del rendimento con gas ideali", "pages":[484,485,500,501,545,443,444,445,446] }, \
{ "id":50, "text":"Secondo Principio della Termodinamica: enunciati di Kelvin e Clausius", "pages":[487,488,489,545,443,444,445,446] }, \
{ "id":51, "text":"Secondo Principio della Termodinamica: Macchine reversibili e irreversibili, macchine di Carnot, disuguaglianza di Clausius", "pages":[490,491,492,493,494,495,496,497,498,545,484,485] }, \
{ "id":52, "text":"Entropia: definizione macroscopica, entropia di un gas ideale, cenni di interpretazione microscopica", "pages":[500,501,502,503,504,505,506,507,508,509,510,511,545,484,485,490,491,492,493,494,495,496,497,498] }, \
{ "id":53, "text":"Cicli frigorigeni e coefficiente di prestazione", "pages":[516,517,518,519,520,545,484,485,500,501] }, \
{ "id":54, "text":"Trasmissione del calore: conduzione, convezione, irraggiamento", "pages":[527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,545,424,425,426,427,428,429,430,431,432,433,434,435] } \
]} \
] 

#for qg in questiongroups:
#    for q in qg["questions"]:
#        print(q["id"])
#        pdfx.extractpdf(mainfile, './oral-exam-tool/Q_' + str(q["id"]) + '.pdf', q["pages"])

htmlstr = '<html><head><title>Supporto Esame Orale Fisica 1</title></head><body>'
htmlstr = htmlstr + '<script>\n' + \
'const qg = ' + json.dumps(questiongroups) + ';\n\n' + \
'function generatequestion(g) {\n' + \
'  let gro = qg[g - 1];\n' + \
'  let qr = Math.floor(Math.random() * gro["questions"].length);\n' + \
'  document.getElementById("Q_" + g + "_text").innerHTML = "<a target=\\"_blank\\" href=\\"Q_" + gro["questions"][qr]["id"] + ".pdf\\">" + gro["questions"][qr]["id"] + ": " + gro["questions"][qr]["text"] + "</a>";\n' + \
'  document.getElementById("Q_" + g + "_grade").value = "";\n' + \
'}\n\n' + \
'function startexam() {\n' + \
' document.getElementById("name").readOnly = true; let wr = document.getElementById("writtenexam"); wr.readOnly = false; wr.value = ""; document.getElementById("total").value = "";\n' + \
' ["1","2","3"].forEach(la => { document.getElementById("Q_" + la + "_text").innerHtml = ""; let lag = document.getElementById("Q_" + la + "_grade"); lag.readOnly = false; lag.value = ""; });\n ' + \
'}\n\n' + \
'function ongradechange() {\n' + \
' let gw = parseInt(document.getElementById("writtenexam").value); ' + \
' let go = ["1","2","3"].map(q => parseInt(document.getElementById("Q_" + q + "_grade").value)).reduce((ps, acc) => ps + acc, 0); ' + \
' let gavg = Math.round(gw + go) / 2;\n' + \
' document.getElementById("total").value = gavg;\n' + \
'}\n\n' + \
'function stopexam() {\n' + \
' if (confirm("Sei sicuro/a di voler terminare l''esame?") == false) return;\n' + \
' document.getElementById("name").readOnly = false; let wr = document.getElementById("writtenexam"); wr.readOnly = true; document.getElementById("total").readOnly = true;\n' + \
' ["1","2","3"].forEach(la => { document.getElementById("Q_" + la + "_text").readOnly = true; });\n ' + \
'}\n\n' + \
'</script>'
htmlstr = htmlstr + ' <h1>Supporto Esame Orale Fisica 1</h1>'
htmlstr = htmlstr + ' <h2>Candidato/a <input type="text" id="name"></input> <input type="button" value="Inizia" onclick="startexam()"></input></h2>'
htmlstr = htmlstr + ' <h2>Voto scritto <input readonly type="text" id="writtenexam" onchange="ongradechange()"></input></h2>'
htmlstr = htmlstr + ' <hr />'
htmlstr = htmlstr + ' <div id="Q_1"><p><input type="button" onclick="generatequestion(1)" value="Genera domanda 1" /></p><p id="Q_1_text"></p><p>Voto: <input readonly type="number" id="Q_1_grade" onchange="ongradechange()"></input></p></div>'
htmlstr = htmlstr + ' <hr />'
htmlstr = htmlstr + ' <div id="Q_2"><p><input type="button" onclick="generatequestion(2)" value="Genera domanda 2" /></p><p id="Q_2_text"></p><p>Voto: <input readonly type="number" id="Q_2_grade" onchange="ongradechange()"></input></p></div>'
htmlstr = htmlstr + ' <hr />'
htmlstr = htmlstr + ' <div id="Q_3"><p><input type="button" onclick="generatequestion(3)" value="Genera domanda 3" /></p><p id="Q_3_text"></p><p>Voto: <input readonly type="number" id="Q_3_grade" onchange="ongradechange()"></input></p></div>'
htmlstr = htmlstr + ' <hr />'
htmlstr = htmlstr + ' <h2>Voto complessivo <input type="text" id="total" readonly></input> <input type="button" value="Fine" onclick="stopexam()"></input></h2>'
htmlstr = htmlstr + '</body></html>'

with open('./oral-exam-support/oes.html', 'wt') as fout:
    fout.write(htmlstr)