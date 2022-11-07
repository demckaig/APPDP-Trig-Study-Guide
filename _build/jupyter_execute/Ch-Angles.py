#!/usr/bin/env python
# coding: utf-8

# # Angles and the Unit Circle
# In this chapter we will define the *unit circle* and the various ways we make **angular** measurements on it. 

# ## Angle Measurements
# 
# In cartesian space (an $xy$-grid) we define a ray along the $x$ axis to be at zero degrees.
# We can rotate that ray *counter-clockwise* to an angle $\phi$ and sweep around the $xy$ plane.
# 
# ```{figure} ./media/define-angle.svg
# ---
# align: center
# ---
# Counterclockwise rotations are by definition positive (increasing in angle).
# ```
# 
# A complete circle is defined to be $360^\circ$. 
# Manipulate the slider on the next plot to get an idea of where different angular measurements fall on the circle.

# In[1]:


import plotly.graph_objects as go
import numpy as np

# Create figure
fig = go.Figure()

'''
fig.add_trace(
    go.Scatter(
        x=np.cos(np.arange(0, 2*np.pi, 0.01)),
        y=np.sin(np.arange(0, 2*np.pi, 0.01))
    )
)
'''

# Add traces, one for each slider step
for step in np.arange(0, 360+1, 1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#dc5050", width=6),
            name="𝜈 = " + str(step),
            x=np.cos(np.arange(0, step*np.pi/180, 0.01)),
            y=np.sin(np.arange(0, step*np.pi/180, 0.01))))

# Make iith trace visible
fig.data[90].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "φ = : " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=1,
    currentvalue={"prefix": ""},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.update_xaxes(range=[-1.25,1.25])
fig.update_yaxes(range=[-1.25,1.25])
fig.update_yaxes(
    scaleanchor = "x",
    scaleratio = 1,
  )

fig.show()


# 

# ## Arc Length and Radians
# The circumference of a circle is
# ```{math}
# :label: eq-circumference
# C=2\pi r
# ```
# 
# 
# We define a *radian* as the angle swept out by a line equal in length to the radius of the circle.
# 
# ```{figure} ./media/what-is-a-radian.gif
# ---
# align: center
# ---
# One radian is about 57.3 degrees.
# ```
# 
# A radian is the "natural" unit for angles because it defines arcs around a circle in terms of its natural unit, $\pi$.
# We can quickly convert between degrees and radians with
# 
# $$360^\circ=2\pi\,\text{radians}$$
# 
# Given an angle $\phi$ measured in radians, we also define *arc-length* $s$ as the length on the circumference of a circle.
# ```{math}
# :label: eq-arc-length
# s=r\phi
# ```
# 
# Arc-length as a beautifl result that helps us remember it by recognizing that we complete one complete loop, $\phi=2\pi$, we will "travel" an arc-length equal to the circumference. 
# 
# $$\text{Arc-length once around}: s = r(2\pi) = \text{the circumference}$$
# 

# ## Exercises
# 1. A car makes $32^\circ$ turn on a road with a radius of curvature of 115 meters. How far did the car travel on that turn?
#    ```{dropdown} Solution
#    Don't forget to convert the $32^\circ$ to radians! Otherwise your answer will be in the wrong units.
#    
#    $$s=r\phi=(115\text{m})(32^\circ)$$
#    $$=(115\text{m})\left(32^\circ\frac{2\pi}{360^\circ}\right)$$
#    $$= 64.23 \text{m}$$
#    ```
# 
# 2. How many times will 5.5 meter long rope wrap around an axle with a diameter of 8 centimeters?
#    ```{dropdown} Solution
#    Let $L=5.5$ m and note that this will equal some number $N$ multiple of the circumference.
#    
#    $$ L=N \cdot C $$
#    $$ L=N \cdot 2\pi r $$
#    
#    Since we are given the diameter we'll rewrite the previous equation using diameter, 
#    then solve for the number of turns $N$.
#    
#    $$ L=N\cdot \pi D $$
#    $$ N=\frac{L}{\pi D}$$
#    $$ N=\frac{(5.5\,\text{m})}{\pi (0.08\,\text{m})} $$
#    $$ N=21.8 $$
#    ```
