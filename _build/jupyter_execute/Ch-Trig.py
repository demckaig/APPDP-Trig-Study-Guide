#!/usr/bin/env python
# coding: utf-8

# # Trigonometry
# It is **impossible** to overstate how crucial right triangles and trigonometry are to our knowledge in physics.
# From analyzing vector motions to modelling the quantum mechanical interactions of atoms, trigonometry is **always** present. 
# In this chapter you will find a brief overview of the crucial aspects of trigonometry. 

# ## Right Triangles
# A right triangle is any triangle were one of the interior angles in $90^\circ$. 
# We often label one of the angles of the triangle with a greek theta, $\theta$,
# and discuss the sides of the triangle relative to $\theta$.
# 
# ```{figure} ./media/triangle-45_30-60-90.svg
# ---
# name: fig-basic-right-triangles
# align: center
# ---
# The 45-45 and 30-60-90 triangles frequently occur in physics, so it is convenient to have them for quick reference.
# ```
# 
# In general we describe the edges of a right triangle as the side adjacent to the given angle,
# or opposite the given angle. The longest edge is called the hypotenuse.
# ```{figure} ./media/right-triangle.svg
# ---
# name: fig-right-triangle
# align: center
# ---
# The names of the right triangle sides are relative to the angle $\theta$.
# ```
# 
# Figure {numref}`fig-Pythagorean` visual demonstration of the  *Pythagorean theorem*.
# 
# ```{admonition} Pythagorean theorem
# $$ a^2+b^2=c^2 $$ (eq-Pythag-thrm)
# ```
# 
# ```{figure} ./media/Pythagorean.svg
# ---
# name: fig-Pythagorean
# align: center
# width: 350px
# ---
# With some clever rearranging, it can be shown the blue square and the red square are equal to the purple square.
# ```

# ## SOH-CAH-TOA
# Figure {numref}`triangle-inscribed` shows a right triangle of arbitrary angle inscribed in a circle.
# 
# ```{figure} ./media/inscribed-triangle.svg
# ---
# name: triangle-inscribed
# align: center
# width: 300px
# ---
# If $\theta=0^\circ$ than $x$ will be the radius of the circle and $y=0$.
# ```
# 
# The first three trigonometric functions are defined using this figure,
# 
# ```{math}
# :label: eq-trig-func-def
# \begin{matrix}
# \text{Sine} & \sin\theta = \dfrac{y}{r} \\
# \text{Cosine} & \cos\theta = \dfrac{x}{r} \\
# \text{Tangent} & \tan\theta = \dfrac{y}{x} \\
# \end{matrix}
# ```
# These definitions can be remembered with the mneumonic **SoH-CaH-TOA**.
# **S**ine is **o**pposite over **h**ypotenuse, 
# **C**osine is **a**djacent over **h**ypotenuse, 
# **T**angent is **o**pposite over **a**djacent.
# 
# Now apply the Pythagorean theorem to the trianlge in figure {numref}`triangle-inscribed`,
# 
# $$x^2+y^2=r^2$$
# $$(r\cos\theta)^2+(r\sin\theta)^2=r^2$$
# and we derived our first Trig. Identity!
# 
# $$\sin^2\theta + \cos^2\theta = 1 $$ (trig-ident)
# 

# ## Plotting Trig Functions
# Here are plots of sine, cosine, and tangent along the circle (0 to $2\pi$).
# They are periodic functions, meaning that they repeat every $2\pi$ radians. 
# Notice that tangent diverges at $\pi/2$ and $3\pi/2$, angles corresponding to $x=0$.

# In[1]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
phi=np.arange(0,2*np.pi,.01)

fig = make_subplots(rows=3, cols=1,
        subplot_titles=("Sine","Cosine","Tangent")
                   )

fig.add_trace(go.Scatter(x=phi,y=np.sin(phi)),row=1,col=1)
fig.add_trace(go.Scatter(x=phi,y=np.cos(phi)),row=2,col=1)
fig.add_trace(go.Scatter(x=phi,y=np.tan(phi)),row=3,col=1)
fig.update_yaxes(range=[-10,10],row=3,col=1)
fig.update_layout(showlegend=False)
fig.update_layout(height=800,width=600)
fig.show()


# ## Exercises
# 1. An airplane travelled 500 km going 18$^\circ$ south of east.
#    How far east and how far south did it go?
#    ```{dropdown} Solution
#    $$\text{East} = (500\,\text{km})\cos(18^\circ)=475.528\,\text{km} $$
#    
#    $$\text{South} = (500\,\text{km})\sin(18^\circ)=154.508\,\text{km} $$
#    ```
#    
# 2. A certain time of the day, a tall tree cast a shadow that is 6.35 meters
#    long on the ground. At the same time, a meter stick cast a shadow that is
#    29 centimeters long. How tall is the tree?
#    
#    ```{dropdown} Solution
#    The trick here is to recognize that the angle made by the meter stick and
#    the tree are identical.
#    
#    ![Tree-height](./media/tree-height.svg)
#    
#    We know the adjacent and opposite side lengths for the meter stick triangle,
#    so we will use tangent to determine the tree's height.
#    
#    $$ \text{Meter Stick: } \tan\theta=\frac{1\,\text{m}}{.29\,\text{m}} $$
#    $$ \text{Tree: } \tan\theta=\frac{h}{6.35\,\text{m}} $$
#    $$ \frac{1\,\text{m}}{.29\,\text{m}} = \frac{h}{6.35\,\text{m}} $$
#    $$ h = \frac{1\,\text{m}}{.29\,\text{m}} (6.35\,\text{m}) $$
#    $$ h = 21.90\,\text{m} $$
#    ```
