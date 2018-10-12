#Do you know which is the most inhabited planet I know?
#YURANO

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
