# Met dit programma kan je gemakkelijk afleveringen van Het Bureau luisteren
# op de site van NTR. Het is aan te bevelen om dan wel bij 'firefox' het juiste
# bestandspad in te vullen.

from subprocess import call

bestand = 'bureau.txt'
firefox = "C:/Program Files (x86)/Mozilla Firefox/firefox.exe"

def aflevering(huidige_afl, prompt=''):
	"""Hiermee wordt om een getal gevraagd dat vervolgens kan worden gebruikt om\

	een aflevering mee te openen. De functie controleert of er wel een getal wordt\
	ingegeven. Als er een getal is ingegeven dan moet deze tussen 1 en 287 liggen."""
	nr = raw_input(prompt)
	if nr.capitalize() == 'Stop':
		return nr.capitalize()
	elif nr == '':
		return int(huidige_afl)
	
	else:
		try:
			if int(nr) in range(1, 288):
				return int(nr)
			else:
			 	return aflevering(1, 'Geef een getal tussen 1 en 287: ')
		except:
			return aflevering(1, "Geef een getal op, of typ 'Stop': ")

print """Typ een nummer om daarmee een aflevering van Het Bureau te openen.
Typ 'Stop' om dit programma af te sluiten."""

try:
	with open(bestand) as f:
		huidige_afl = f.read()
	prompt = 'Druk op ENTER om door te gaan met aflevering %d. ' % (int(huidige_afl) % 287)
except:
	huidige_afl = 1
	prompt = 'Druk op ENTER om te beginnen met aflevering 1. '

while True:
	nr = aflevering(huidige_afl, prompt)
	if nr == 'Stop':
		break
	else:
		open_url = "http://audio.omroep.nl/ntr/hetbureau/mp3/%02d.mp3" % nr
		#print open_url #voor het testen
		call([firefox, open_url])
		nr += 1
		prompt = 'Druk op ENTER voor aflevering %d. ' % (nr % 287)
		huidige_afl = str(nr)
		with open(bestand, 'w+') as f:
			f.write(huidige_afl)

print 'Tot ziens'