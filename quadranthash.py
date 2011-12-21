#!/usr/bin/python

import sys
from itertools import imap

def show(matrix):
    # Print out matrix
    skip = True
    for col in matrix:
	if (skip):
	    skip =False
	    continue
	print col
    print ''

def getquad(x,y):
    if x>0 and y>0:
	return 1
    elif x<0 and y<0:
	return 3
    elif x>0 and y<0:
	return 4
    elif x<0 and y>0:
	return 2
    else:
	pass

def queryC(quadMap,i,j):
    quad_count =[0,0,0,0]
    quad_count[0] = quadMap[1][j]-quadMap[1][i-1]
    quad_count[1] = quadMap[2][j]-quadMap[2][i-1]
    quad_count[2] = quadMap[3][j]-quadMap[3][i-1]
    quad_count[3] = quadMap[4][j]-quadMap[4][i-1]
    print ' '.join(imap(str,quad_count))

def flipY(quadMap,i,j):
    for idx in xrange(i,j+1):
	if quadMap[0][idx] == 1:
	    updateQuadHash(quadMap,idx,2)
	elif quadMap[0][idx] == 2:
	    updateQuadHash(quadMap,idx,1)
	elif quadMap[0][idx] == 4:
	    updateQuadHash(quadMap,idx,3)
	elif quadMap[0][idx] == 3:
	    updateQuadHash(quadMap,idx,4)
	else:
	    pass
    batchupdate(quadMap,j+1)

def flipX(quadMap,i,j):
    for idx in xrange(i,j+1):
	updateQuadHash(quadMap,idx,5-quadMap[0][idx])
    batchupdate(quadMap,j+1)

def batchupdate(quadMap, j):
    for i in xrange(j,len(quadMap[0])):
	quadMap[1][i] = quadMap[1][i-1]
	quadMap[2][i] = quadMap[2][i-1]
	quadMap[3][i] = quadMap[3][i-1]
	quadMap[4][i] = quadMap[4][i-1]
	quadMap[quadMap[0][i]][i] +=1

def updateQuadHash(quadMap, i,quad):
    quadMap[0][i] = quad
    
    # copy the last point distribution hashtable
    quadMap[1][i] = quadMap[1][i-1]
    quadMap[2][i] = quadMap[2][i-1]
    quadMap[3][i] = quadMap[3][i-1]
    quadMap[4][i] = quadMap[4][i-1]
    
    # update the point distribution hashtable
    quadMap[quad][i] +=1
    # show(quadMap)

def main():

    points = sys.stdin.readlines()
    input_size = int (points[0])
    # data structure for quads, it's a Nx5 matrix where first colum is the quad the point lies in  
    quadMap= [[0 for row in xrange(input_size+1)] for col in xrange(5)]

    for i in xrange(1,input_size+1):
	sp = points[i].strip().split()
	x = int (sp[0])
	y = int (sp[1])
	quad = getquad(x,y)
	updateQuadHash(quadMap,i,quad)

    query_size = int(points[input_size+1])
    for k in xrange(input_size+2,input_size+2+query_size):
	sp = points[k].strip().split()
	command = sp[0]
	i = int (sp[1])
	j = int (sp[2])
	if ('C' == command ):
	    queryC(quadMap,i,j)
	elif ('X' == command ):
	    flipX(quadMap,i,j)
	elif ('Y' == command ):
	    flipY(quadMap,i,j)
	else:
	    pass

    sys.stdout.flush()


if __name__ == '__main__':
    main()

