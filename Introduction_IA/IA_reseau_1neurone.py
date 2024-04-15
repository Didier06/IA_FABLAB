from keras.models import Sequential 
from keras.layers import Dense 
from keras import initializers
from keras.optimizers import SGD, Adam

#my_init = initializers.Zeros() 
my_init = initializers.Ones()
#my_init = initializers.RandomUniform(minval=0.0, maxval=1.0)
#normalizer = preprocessing.Normalization()
model=Sequential() # network with linear layer only
#pour La couche d'entrée, input_shape doit être égale à 1 + couche 3 neurones units = 3
model.add(Dense(units=1,input_shape=[1],activation= 'linear',kernel_initializer = my_init))

entree=([1,2,3,4,5,6])
sortie=([3,6,9,12,15,18])

#Création du réseau ("adam "alternatif à "sgd")
#opt = SGD(learning_rate=0.01) #w = w - learning_rate * gradient

opt = Adam(learning_rate=0.5) # learning rate : pas d'apprentissage pour la correction de l'erreur
model.compile(loss='mean_squared_error',optimizer=opt)

#Entraînement du réseau 100 passages
model.fit(x=entree,y=sortie,epochs=100)

#Print weights
print("")
print("Weights: \n")
print(model.get_weights())
#Prédire les nombres
print("prédictions  :\n")
print(model.predict([6]))
print(model.predict([7]))
print(model.predict([8]))