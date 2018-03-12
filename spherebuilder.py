import math
import numpy as np
import icostables


def crt2SphPol(cart):
	x = cart[0]
	y = cart[1]
	z = cart[2]
	r = math.sqrt(x*x+y*y+z*z)
	t = math.acos(z/(r))
	p = math.atan2(y,x)
	return(r,t,p)

def sphPol2Crt(sph):
	r = sph[0]
	t = sph[1]
	p = sph[2]
	x = r*math.sin(t)*math.cos(p)
	y = r*math.sin(t)*math.sin(p)
	z = r*math.cos(t)
	return(x,y,z)

def cartDistMag(a,b):
	return np.sum(map(lambda a,b: (a-b)**2,a,b))


def coverSphere(radius,coords):
	newCoords = []
	for c in coords:
		cSph = crt2SphPol(c)
		cSphNew = (radius,cSph[1],cSph[2])
		newCoords.append(sphPol2Crt(cSphNew))
	return newCoords

def getMinimumRadius(coords):
	minD = cartDistMag(coords[0],coords[1])
	for i in range(len(coords)):
		for j in range(i+1,len(coords)):
			c1 = coords[i]
			c2 = coords[j]
			d = cartDistMag(c1,c2)
			if d < minD:
				minD = d
	return minD


def cover72Sphere(radius):
	return coverSphere(radius,icostables.icos72)

def cover92Sphere(radius):
	return coverSphere(radius,icostables.icos92)

def cover122Sphere(radius):
	return coverSphere(radius,icostables.icos122)

def cover132Sphere(radius):
	return coverSphere(radius,icostables.icos132)

def lammpsPrint(coords):
	atomNum = 2902
	for c in coords:
		line = str(atomNum)+" 3 "+str(c[0])+" "+str(c[1])+" "+str(c[2]+8) + "   1 1 0   0 0 0"
		atomNum +=1
		print(line)


def main():
	# for i in range(2921,2973):
	# 	print(str(i)+'')
	lammpsPrint(cover72Sphere(4.0))

if __name__== "__main__":
  main()