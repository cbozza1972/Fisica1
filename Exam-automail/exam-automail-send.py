import pyexcel
from pyexcel_ods import get_data
import sys
import os
import exam_automail_mailer as eam

# Open the ODS file
data = get_data(sys.argv[1])
gradesheet = data['Foglio1']
#print(json.dumps(data))
cands = []
commentcols = []
wflag = False
for grow in gradesheet:
        if wflag:
                if grow[0] == 'END':
                        break
                else:
                       cands.append( \
                        {"Name":grow[0], \
                        "Email":grow[2], \
                        "Grade":grow[-2], \
                        "Result":grow[-1], \
                        "Comments":[c["RemarkHeader"] + ": " + grow[c["Column"]] for c in commentcols], \
                        "File":os.path.join(sys.argv[2],grow[0].replace(' ','_') + '.pdf')})              
                       if os.path.exists(cands[-1]["File"]) == False:
                                raise ValueError("Cannot find file: " + cands[-1]["File"])
        if grow[0] == 'Candidato':
                wflag = True
                for i in range(0,len(grow)):
                        if "Commento" in grow[i]:
                                commentcols.append({"RemarkHeader":grow[i],"Column":i})

print(cands)

for cand in cands:
        eam.SendMessage('cbozza@unisa.it',cand["Email"],'Risultato prova scritta Fisica 1', \
                "Gentile " + cand["Name"] + "<br /><br />" + \
                "Il risultato della sua prova scritta è stato giudicato con voto pari a " + str(cand["Grade"]) + " " + \
                cand["Result"] +" per la prova orale.<br />" + \
                "<br />".join(cand["Comments"]) + "<br />" + \
                "<br />In allegato può trovare copia del Suo elaborato. <br />" + \
                "Cordiali saluti <br /><br />Cristiano Bozza", \
                "Gentile " + cand["Name"] + "\n\n" + \
                "Il risultato della sua prova scritta è stato giudicato con voto pari a " + str(cand["Grade"]) + " " + \
                cand["Result"] +" per la prova orale.\n" + \
                "\n".join(cand["Comments"]) + "\n" + \
                "\nIn allegato può trovare copia del Suo elaborato. \n" + \
                "Cordiali saluti \n\nCristiano Bozza", \
                cand["File"])

