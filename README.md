#Do you know which is the most inhabited planet I know?
#YURANO

DEVI PRIMA DI TUTTO SCARICARTI I DATA DA KAGGLE SE NON CE LI HAI GIÀ, 
PER SICUREZZA SONO QUELLI COMPOSTI DA FILE .csv E CHE ALL' INTERNO dovrebbero aver una
forma di questo tipo:
countrycode,drawing,key_id,recognized,timestamp,word
US,"[[[167, 109, 80, 69,..246, 182, 165], [140, 194, .. 121, 127, 120]], [[207, 207, 210, 221, 238], [74, 103, 114, 128, 135]]]",5152802093400064,True,2017-03-08 21:12:07.266040,airplane

Generate the .npz datasets that will be later used to train the LSTM:
OVVIAMENTE DAI UNA MEZZA OCCHIATA CHE NON HO FATTO ERRORI, CHE SAI COME SONO FATTO...
Allora, qui in poche parole faccio due cose:
- estraggo i dati da data e li metto in liste,
  i tratti spezzati io li ho concatenati con quello successivo, forse si può fare in un altro modo
  tipo avevo pensato una soluzione [x,y,tratto a cui appartiene] invece che solo [x,y]
- carco di correggere le liste che contengono le informazioni di input, 
 in particolare, la lstm per come è fatta vuole dati tutti con lunghezza uguale,
 quindi bisogna spezzare le sequenze troppo lunghe e allungare quelle troppo corte 
 io l'ho fatto nel modo più veloce perchè non avevo cazzi... 
 dentro comunque c'è scritto quello che ho fatto.. se hai voglia di metterti un pò
 a cincionare questa parte può essere un pò migliorata...

~~~~
-python3 generate_npz.py 
~~~~

Train the LSTM that recognizes videos passing as datasets the .npz files
generated in the previous step:
Qui essenzialmente ho riciclato la lstm dell'altra volta, mi sembra funzioni abbastanza bene...
~~~~
python3 train_videos.py 
~~~~

In sti giorni provo a buttare giù il programma per il test set... 
