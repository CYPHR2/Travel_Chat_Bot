import aiml
import os

mybot = aiml.Kernel()
mybot.learn("startup.xml")
mybot.respond("test.aiml")

while True:
    print (mybot.respond(input("Talk to J.A.R.V.I.S: ")))	