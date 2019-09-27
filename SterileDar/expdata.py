import math
class expdata:
	def __init__(self, *args, **kwargs):
       	# you can add additional code here if needed
               	pass

	mmparafin = 352.68	#g/mol
	dparafin = 900*10e3	#g/m³
	mmlab = 260.46	#g/mol
	dlab = 863*10e3	#g/m³
	mmppo = 221.25	#g/mol
	dppo = 1.1*10e6	#g/m³
	r = 4	#m
	h = 20.5	#m

	vtotal=4*(math.pi)*(r**2)*h

	mol=6.02*10e23

	vparafin=vtotal*0.15#m3
	vppo=vtotal*0.03#m3
	vlab=vtotal*0.847#m3

	massparafin=vparafin*dparafin#g
	massppo=vppo*dppo#g
	masslab=vlab*dlab#g

	molparafin=massparafin/mmparafin
	molppo=massppo/mmppo
	mollab=masslab/mmlab
	
	moleculaparafin=mol*molparafin
	moleculappo=mol*molppo
	moleculalab=mol*mollab

	carbonoparafin=25*moleculaparafin
	carbonolab=19*moleculalab
	carbonoppo=15*moleculappo
	carbonototal=carbonoparafin+carbonolab+carbonoppo

	hidrogenioparafin=52*moleculaparafin
	hidrogeniolab=32*moleculalab
	hidrogenioppo=11*moleculappo
	hidrogeniototal=hidrogenioparafin+hidrogeniolab+hidrogenioppo

	nitrogeniototal=1*moleculappo

	oxigeniototal=1*moleculappo

