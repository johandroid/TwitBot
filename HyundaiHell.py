#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random,tweepy, time, sys

#argfile = str(sys.argv[1])

cuentas1=["@HyundaiEsp","@HyundaiPR_es"]
cuentas2=[	"@automobilebcn","@kiamotorsiberia","@autopista_es","@MINIEspana","@Mitsubishi_ES","@revistaCAR","@DS_Espana","@TheLuxonomist", 
			"@MacaLVaraCAR","@skoda_es", "@EFE_motor", "@PrensaRENAULT", "@cochesnet", "@AlfaRomeo_es","@Toyota_Esp", "@Toyota_Esp", "@BMWEspana","@TeslaMotors"]
htags=["#NoComprarIoniq","#HyundaiNoResponde","#NoComprarHyundai","#RespetoAlComprador","#DevoluciónYa","#PesimIoniq"]
#enter the corresponding information from your Twitter application:
mensajes=[	"Me duró dos días el coche y de resto en taller", "Más de 15 días en taller y no me quisieron hacer cambio o devolución","El peor servicio postventa!",
			"Pésimo servicio postventa en Terrassa!", "La batería le duro muy poco, malísimas!","Tras 2 días y el coche en taller con check engine permanente","Falso el consumo 'homologado' del IONIQ ",
			"He conducido el coche muy pocos días porque no para de fallar","Hyundai no devuelve el dinero ni hace cambio de productos defectuosos!","Cuidado con Hyundai!","No compren Ioniq",
			"Como ingeniero puedo decir que Hyundai Ioniq es pésimo!","Cuidado no compren nada de Hyundai, sale pésimo!","Hyundai no respeta a sus clientes"]
CONSUMER_KEY = 'uFXwHqAaHZQEmINqS34JoM6Ys'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'Z1iSOZ405f5DOo2I5n6Uo4v5JZnMtfmiKOUOGO841VNVcJG1CJ'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '96755262-JpsdkB9pf9xXeZVfXPF8hpZtEEybZzlwHzQ5xn6e7'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'gqqb5zLRm6hAd86BlMQ6lTEhWaIzdeSe64I3N5WckDzlj'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()

countdown=70
while countdown > 0:
    tocarhuevos=random.choice(cuentas1)+" "+random.choice(cuentas2)+" "+random.choice(mensajes)+" "+random.choice(htags)
    print tocarhuevos
    duermo=random.randint(2500,3200)
    print duermo
    time.sleep(duermo)#Tweet every 15 minutes
    api.update_status(tocarhuevos)
    countdown=countdown-1