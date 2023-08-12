get_data:- write('Patients name:'),nl,read(P),hypothesis(P,D),!,write(P),tab(9),write('Probably has disease:'),write(D),nl.

get_data:- nl,write('We are sorry we cannot diagnose disease'),nl.

symptom(P,fever):- write('Does '),write(P),write(' have a fever?(y/n):'),read(R),R='y'.
symptom(P,cough):- write('Does '),write(P),write(' have a cough?(y/n):'),read(R),R='y'.
symptom(P,runnynose):- write('Does '),write(P),write(' have a runnynose?(y/n):'),read(R),R='y'.
symptom(P,sneezing):- write('Is '),write(P),write(' sneezing?(y/n):'),read(R),R='y'.
symptom(P,rash):- write('Does '),write(P),write(' have a rash?(y/n):'),read(R),R='y'.
symptom(P,headache):- write('Does '),write(P),write(' have a headache?(y/n):'),read(R),R='y'.
symptom(P,bodyache):- write('Does '),write(P),write(' have a bodyache?(y/n):'),read(R),R='y'.

hypothesis(P,measels):- symptom(P,fever),symptom(P,rash),symptom(P,cough).

hypothesis(P,flu):- symptom(P,fever),symptom(P,headache),symptom(P,bodyache),symptom(P,runnynose),symptom(P,cough).

hypothesis(P,common_cold):- symptom(P,headache),symptom(P,sneezing),symptom(P,cough),symptom(P,runnynose).

