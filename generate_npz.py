import numpy as np

import csv
import ast
import os

counter=0
video_folder="data"

MAX_LENGTH_SENT=100

images_train=[]
labels_train=[]
images_dev=[]
labels_dev=[]
classes=[]

for filename in os.listdir(video_folder):
    classes.append(filename)

#QUI ESTRAGGO I LE INFO DA DATA
#for filename in os.listdir(video_folder): #SE SI VOGLIONO  FARE TUTTE LE CLASSI INVECE CHE LE PRIME DIECI
for filename in os.listdir(video_folder)[0:10]:
    print filename,classes.index(filename)
    with open(os.path.join(video_folder,filename), 'rb') as csvfile:
        spamreader = list(csv.reader(csvfile))
        for row in spamreader:
            if row[1].startswith("["):
                image=[]    #tutti i pixel sono concatenati quindi non considero pixel spezzati
                #TODO: aggiungere oltre a x e y anche un contatore di tratti ????
                image_spezzata=[]
                for segm in ast.literal_eval(row[1]):
                    tratto=[]
                    #print segm
                    for x,y in zip(segm[0],segm[1]):
                        image.append([x,y])
                        tratto.append([x,y])
                    image_spezzata.append(tratto)
                #print "image tutta concatenata", image
                #print "image spezzata", image_spezzata
                #print ""
                #images.append(ast.literal_eval(row[1]))
                #QUI COSTRUISCO DEV SET CON IL 20% DEI DATI
                if counter % 10<8:
                    images_train.append(image)
                    labels_train.append(classes.index(filename))
                else:
                    images_dev.append(image)
                    labels_dev.append(classes.index(filename))
                counter+=1
#print counter

#VOLENDO ESISTE ANCHE LA LSTM CHE CONSIDERA LUNGHEZZE DINAMICHE... MA DIO CAN

def create_sequence_same_length(sequenceX, sequenceY, maxlen):
    # FIRST PHASE : CREATE NEW SEQUENCE WHERE ALL ELEMENTS HAVE LENGTH MINUS MAX
    new_seqX = []
    new_seqY = []
    # valide alternative:
    # 1- prendere uno si uno no e uno no uno si e creare cosi due nuove sequenze
    # 2- dividere a meta' la sequenza(sarebbe meglio tenere conto dei tratti)
    #  si puo' mettere anche entrambi i modi ...
    for el, lab in zip(sequenceX, sequenceY):
        if len(el) > maxlen:
            if len(el) % maxlen == 0:
                rapporto = len(el) // maxlen
            else:
                rapporto = len(el) // maxlen + 1
            for r in range(rapporto):
                if (r + 1) * maxlen < len(el):
                    new_seqX.append(el[r * maxlen:(r + 1) * maxlen])
                    new_seqY.append(lab)
                else:
                    new_seqX.append(el[r * maxlen:len(el)])
                    new_seqY.append(lab)
        else:
            new_seqX.append(el)
            new_seqY.append(lab)
    # SECOND PHASE : all elements too short are enlonged
    new_seqX_ = []
    new_seqY_ = []
    # valide alternative:
    # scelgo di ripetere l'ultimo punto trovato (QUELLO FATTO FINO AD ADESSO)
    #TODO: forse ha senso eliminare la lista se la sua lunghezza troppo corta...
    #eventualmente al posto di ripetere l'ultimo elemento si puo' pensare di riscrivere gli elementi in ordine opposto
    for el, lab in zip(new_seqX, new_seqY):
        if len(el) < maxlen:
            last_element=el[len(el)-1]
            while len(el)<maxlen:
                el.append(last_element)
            new_seqX_.append(el)
            new_seqY_.append(lab)
        else:
            new_seqX_.append(el)
            new_seqY_.append(lab)

    return new_seqX_, new_seqY_

images_train,labels_train=create_sequence_same_length(images_train,labels_train,MAX_LENGTH_SENT)
images_dev,labels_dev=create_sequence_same_length(images_dev,labels_dev,MAX_LENGTH_SENT)

print len(images_dev),len(labels_dev)
print len(images_train),len(labels_train)

for el in images_train:
    if not len(el) == MAX_LENGTH_SENT:
        print len(el)
for el in images_dev:
    if not len(el) == MAX_LENGTH_SENT:
        print len(el)

#SALVO INFO NEI FILE...
np.savez("data_npz/train_.npz", images=images_train, images_y=labels_train)
np.savez("data_npz/dev_.npz", images=images_dev, images_y=labels_dev)