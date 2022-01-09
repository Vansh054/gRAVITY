import pandas as pd 
import math

df = pd.read_csv("main.csv")

mass = df['Mass'].tolist()
radius = df['Radius'].tolist()

new_mass = []
new_radius = []
gravity = []

for i in range (1,50,2) :
    m = float(mass[i])*1.989e+30
    new_mass.append(m)
    r = float(radius[i])*6.957e+8
    new_radius.append(r)
    g = 6.67 * pow(10,-11) * (m/r**2)
    gravity.append(g)

newdf = pd.DataFrame({"Radius" : new_radius,"Mass" : new_mass,"Gravity" : gravity})
newdf.to_csv("calculated.csv")


