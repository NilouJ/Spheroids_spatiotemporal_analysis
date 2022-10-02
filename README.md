# Spheroid (3D) and monolayer cells (2D) Spatiotemporal analysis
## Mass balance equation of transport in 2D monolayer cells

The transport of nanocarriers in 2D monolayer cells has been modeled by lumped assumption. The changes in the accumulation of drug/particles during the time in this system “lumped into a point” is equal to the input rate of mass flow. Applying the mass transfer balance to this system we reach:

$$Eq.1\quad\quad\quad\quad\ v\frac{\partial(C(t))}{\partial(t)}=mkACt $$

Where C(t) is the concentration of drug/particle during the time, kc is the mass transfer coefficient, m is the mass, and v and A represents the volume and area of the cells. The solution to this simple first-order ordinary differential equation is as follows:


$$Eq.2\quad\quad\quad\quad\ C(t)={e}^{-\tau t}\quad\quad\quad\quad\tau=\frac{mkA}{v}$$

Therefore, the concentration of diffusive drug/particle increases exponentially over time. The time constant τ is proportional to the mass transfer coefficient kc. 

![image](https://user-images.githubusercontent.com/113156852/193437761-ef591288-a700-4954-b432-e316b31909a3.png)


## Mass balance equation of transport in 3D spheroids
For 3D geometry, we have simplified the mass transport as a 1-dimensional (radial) unsteady (dynamic – varying with time) diffusion problem in Figure 1. The dominant mass transport mechanism into a spheroid is diffusion. 


![image](https://user-images.githubusercontent.com/113156852/193436657-635487f1-2c03-48d5-982d-40d097f348d1.png) 

Here, we model the dynamic nano drugs diffusion from the surrounding cell culture media into the spheroids. Then, we fit the experimental data to the mathematical model to acquire the actual apparent diffusion coefficient profile. 
The mass balance on the diffusion-controlled accumulation of nano drugs in spheroid by applying the first Fick’s law gives:

$$Eq.3\quad\quad\quad\quad\ \frac{\partial(C(t))}{\partial(t)}=Dcoeff.{\nabla}^{2}C $$

Where C is the concentration and Dcoeff is the diffusion coefficient of nano drugs in spheroids. To expand the gradient term, we make a few assumptions. According to Figure 1, we assume symmetrical radial diffusion of nano drugs into the spheroid. Next, we assume that the spheroid is immersed in a semi-infinite liquid with a constant concentration of diffusant; the corresponding radial unsteady diffusion transport process is described as:


$$Eq.4\quad\quad\quad\quad\  \frac{\partial(C(t))}{\partial(t)}=\frac{Dcoeff.}{{r}^{2}}\frac{\partial}{\partial(r)}({r}^{2}\frac{\partial C}{\partial(r)}) $$

To solve this parabolic partial differential equation, we need two BCs in the radial direction and one IC. For the current model, we assume that the concentration of the diffusant is a function of time at the surface of the sphere and is bounded or limited at the center of the spheroid, we have:

$$IC:\quad\quad\quad\quad\ C(r,0)=f(r)\quad\quad\ @t=0  $$

$$BC1:\quad\quad\quad\quad\ C(R,t)=g(t)\quad\quad\ @r=R  $$

$$BC2:\quad\quad\quad\quad\ \frac{\partial(C(0,t))}{\partial(t)}==0\quad\quad\ @r=0  $$

The analytical solution of this equation (Equation 4) :

$$Eq.5\quad\quad\quad\quad\  \frac{\partial(C(r,t)-CR)}{\partial(C0-CR)}=\frac{2r}{\pi r}\displaystyle\sum_{n=1}^{n} \frac{{-1}^{n+1}}{n}\sin(\frac{\pi n r}{R})exp(-\frac{Dcoeff. \pi^2 n^2}{R^2} t)$$

Therefore, the analytical values of concentration profiles at each timepoint are known theoretically and after fitting the corresponding concentration radial profiles. 

We have estimated the value of Dcoeff at each radius or distance from the spheroid core to plot the radial profiles of the diffusion coefficient. 

![image](https://user-images.githubusercontent.com/113156852/193437834-ed7968ad-06ce-4897-8613-0b1474f68c13.png)




