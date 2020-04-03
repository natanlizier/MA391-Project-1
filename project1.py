# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:37:01 2020

@author: Natan LZ
"""
import matplotlib.pyplot as plt
##1.00133851189 -> decimal that to the 17th equals 1.023
##needed to know chance of dying each die once quarantined





####
#Assumption Variables
####
#average number of people someone infects while in incubation 
#must divide by incubation days
IC = 4.2
#chance of dying
#(DC+1)^infected = actual percent chance of dying before full recovery
#example -> chance of death equal 2.3% would make DC equal to .0013385
DC = .002069
# days in incubation
DI = 14
# days infected post incubation
PI = 11
#number of people that start out infected
initial = 30

def model(IC,DC,DI,PI,initial,N):
    recov = [0];dead = [0];infected=[0];totalRecov = [0];totalDead = [0];time = [0]
    t = 0;sus = 7500000000-initial
    susList = [sus]
    incub = [0]*DI
    incub[0]=initial
    infect = [0]*PI
    while t < N:
        t += 1
        while t < DI:
            x = sum(incub)
            if sus - x*IC > 0:
                incub[t]=x*IC
                sus -= x*IC
                susList.append(sus)
                time.append(t)
                t+=1
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(0)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
            if sus - x*IC <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                time.append(t)
                t+=1
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(0)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
        while t < (DI+PI):
            quarantine = incub[t%DI]
            x = sum(incub)
            if sus - x*IC > 0:
                incub[t%DI] =x*IC
                sus -=x*IC
                susList.append(sus)
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
            if sus - x*IC <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
        while t < N:
            quarantine = incub[t%DI]
            x = sum(incub)
            if sus - x*IC > 0:
                incub[t%DI] =x*IC
                sus -=x*IC
                susList.append(sus)
                recovered = infect[(t-DI)%PI]
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(recovered)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
            if sus - x*IC <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                recovered = infect[(t-DI)%PI]
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(recovered)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))            
                time.append(t)
                t+=1            
    return(time,dead,recov,infected,totalDead,totalRecov,susList)
    
def socialDistance(IC,DC,DI,PI,initial,N):
    recov = [0];dead = [0];infected=[0];totalRecov = [0];totalDead = [0];time = [0]
    t = 0;sus = 7500000000-initial
    susList = [sus]
    incub = [0]*DI
    incub[0]=initial
    infect = [0]*PI
    while t < N:
        t += 1
        while t < DI:
            x = sum(incub)
            if sus - x*IC > 0:
                incub[t]=x*IC
                sus -= x*IC
                susList.append(sus)
                time.append(t)
                t+=1
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(0)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
            if sus - x*IC <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                time.append(t)
                t+=1
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(0)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
        while t < (DI+PI):
            quarantine = incub[t%DI]
            x = sum(incub)
            if sus - x*IC/4 > 0:
                incub[t%DI] =x*IC/4
                sus -=x*IC/4
                susList.append(sus)
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
            if sus - x*IC/4 <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(0)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
        while t < N:
            quarantine = incub[t%DI]
            x = sum(incub)
            if sus - x*IC/4 > 0:
                incub[t%DI] =x*IC/4
                sus -=x*IC/4
                susList.append(sus)
                recovered = infect[(t-DI)%PI]
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(recovered)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))
                time.append(t)
                t+=1
            if sus - x*IC/4 <= 0:
                incub[t%DI] = sus
                sus -= sus
                susList.append(sus)
                recovered = infect[(t-DI)%PI]
                infect[(t-DI)%PI] = quarantine
                alive = sum(infect)
                infect = [i-(DC*i) for i in infect]
                stillAlive = sum(infect)
                died = alive-stillAlive
                infected.append(sum(incub)+sum(infect))
                recov.append(recovered)
                dead.append(died)
                totalRecov.append(sum(recov))
                totalDead.append(sum(dead))            
                time.append(t)
                t+=1            
    return(time,dead,recov,infected,totalDead,totalRecov,susList)
    
def regScale(time,dead,recov,infected,totalDead,totalRecov,susList):
    ax = plt.subplot(1,1,1)            
    ax.plot(time,dead,label='Dead/day')
    ax.plot(time,recov,label='Recovered/day')
    ax.plot(time,infected,label='Total Infected')
    ax.plot(time,totalDead,label='Total Dead')
    ax.plot(time,totalRecov,label='Total Recovered')
    ax.plot(time,susList,label='Susceptible')
    ax.set_title('Regular Scale')
    ax.legend(loc ='upper center',bbox_to_anchor=(0.5, -0.05))
    plt.show()

def logScale(time,dead,recov,infected,totalDead,totalRecov,susList):
    ax1 = plt.subplot(1,1,1)
    ax1.semilogy(time,dead,label='Dead/day')
    ax1.semilogy(time,recov,label='Recovered/day')
    ax1.semilogy(time,infected,label='Total Infected')
    ax1.semilogy(time,totalDead,label='Total Dead')
    ax1.semilogy(time,totalRecov,label='Total Recovered')
    ax1.semilogy(time,susList,label='Susceptible')
    ax1.set_title('Semi-log Scale')
    ax1.legend(loc ='upper center',bbox_to_anchor=(0.5, -0.05))
    plt.show()

IC=0.3;DC=.002069;DI=14;PI=11;initial= 30;N=102
time,dead,recov,infected,totalDead,totalRecov,susList=model(IC,DC,DI,PI,initial,N)
time,dead,recov,infected,totalDead,totalRecov,susList=socialDistance(IC,DC,DI,PI,initial,N)
logScale(time,dead,recov,infected,totalDead,totalRecov,susList)
sum(totalDead)+sum(totalRecov)
