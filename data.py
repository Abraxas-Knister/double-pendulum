#!/usr/bin/env python3
from numpy import cos,sin,array,savetxt, zeros,nan
eps = 1

def eom(x,e=False):
    f,t,p,q = x
    cd = cos(f-t)
    det_i = 1./((1+eps)*eps - eps*eps*cd*cd)
    f_dot = det_i * (eps*p - eps*cd*q)
    t_dot = det_i * ((1.+eps)*q - eps*cd*p)
    p_dot = -eps*f_dot*t_dot*sin(f-t) - (1+eps)*sin(f) # the last sine should have 'f' as argument 
    q_dot = eps*f_dot*t_dot * sin(f-t) - sin(t)*eps
    ret = array((f_dot,t_dot,p_dot,q_dot))
    if e: 
        E = (f_dot*p+t_dot*q)/2.-(1.+eps)*cos(f)-cos(t)
        return ret,E
    else: return ret

def rk4(x0,n,f=eom,e=1e-2):
    p = zeros((n,5))
    p[0]=array((0,*x0))
    E = []
    while n-1:
        s,*x = p[-n]
        k1,EE = f(x,True)
        E+=[EE]
        k2 = f(x+k1*e/2.) 
        k3 = f(x+k2*e/2.) 
        k4 = f(x+k3*e)
        x_new = x+e*(k1+k2+k2+k3+k3+k4)/6.
        p[-n+1] = array((s+e,*x_new))
        n-=1
    E+=[nan]
    return p,E

def draw(p,E):
    s = p[:,0]
    f = p[:,1]
    t = p[:,2]
    x1 = sin(f)
    y1 = -cos(f)
    x2 = x1+sin(t)
    y2 = y1-cos(t)
    savetxt('pendata',array((s,x1,y1,x2,y2,E)).T)

draw(*rk4(array((2,3,0,0)),10000))
