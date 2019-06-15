#!/usr/bin/env python3
from numpy import cos,sin,array,savetxt, zeros
eps = 1

def eom(x):
    f,t,p,q = x
    cd = cos(f-t)
    det_i = 1./((1+eps)*eps - eps*eps*cd*cd)
    f_dot = det_i * (eps*p - eps*cd*q)
    t_dot = det_i * ((1.+eps)*q - eps*cd*p)
    p_dot = -eps*f_dot*t_dot*sin(f-t) - (1+eps)*sin(t) 
    q_dot = eps*f_dot*t_dot * sin(f-t) - sin(t)*eps
    return array((f_dot,t_dot,p_dot,q_dot))

def rk4(x0,n,f=eom,e=1e-2):
    p = zeros((n,5))
    p[0]=array((0,*x0))
    while n-1:
        s,*x = p[-n]
        k1 = f(x)
        k2 = f(x+k1*e/2.) 
        k3 = f(x+k2*e/2.) 
        k4 = f(x+k3*e) 
        p[-n+1] = array((s+e,*( x+e*(k1+k2+k2+k3+k3+k4)/6.)))
        n-=1
    return p

def draw(p):
    t = p[:,0]
    f = p[:,1]
    t = p[:,2]
    x1 = -sin(f)
    y1 = -cos(f)
    x2 = x1-sin(t)
    y2 = y1-cos(t)
    savetxt('pendata',array((t,x1,y1,x2,y2)).T)

draw(rk4(array((2,3,0,0)),10000))
