# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:46:21 2013

@author: Will
"""

def Field_Realistic(x,y,z,
    B_xbias,B_ybias,B_zbias, fin_horz_params, fin_vert_params, fin_norm_params):
## ----------Defs
mu=(4*pi)*10^-7 #N/A^2
#Beta=y.^2+z.^2
gridsize = size(x)

## Finite Horizontal wires

#Unpack parameters
LL = fin_horz_params(1,:)
LR = fin_horz_params(2,:)
Y0_fin_horz = fin_horz_params(3,:)
Z0_fin_horz = fin_horz_params(4,:)
I_Guide = fin_horz_params(5,:)

n_fin_horz = size(fin_horz_params)n_fin_horz = n_fin_horz(2)

#preallocate resources
const_G = zeros(size(I_Guide))
B_G = zeros([gridsize,n_fin_horz])
B_Gy = B_G
B_Gz_horz = B_G

for i=1:n_fin_horz
    Beta = (z-Z0_fin_horz(i)).^2 + (y-Y0_fin_horz(i)).^2
    const_G(i)=mu.*I_Guide(i)./(4*pi)
    B_G(:,:,i)=const_G(i).*((x-LL(i))./(Beta.*sqrt(Beta+...
        (x-LL(i)).^2))-(x-LR(i))./(Beta.*sqrt(Beta+(x-LR(i)).^2)))
    B_Gy(:,:,i)=B_G(:,:,i).*(Z0_fin_horz(i)-z)
    B_Gz_horz(:,:,i)=B_G(:,:,i).*(y-Y0_fin_horz(i))
end

## Finite Vertical Wires

#unpack parameters
YD = fin_vert_params(1,:)
YU = fin_vert_params(2,:)
X0_fin_vert = fin_vert_params(3,:)
Z0_fin_vert = fin_vert_params(4,:)
I_Guide = fin_vert_params(5,:)

n_fin_vert = size(fin_vert_params)n_fin_vert = n_fin_vert(2)

#preallocate resources
const_G = zeros(size(I_Guide))
B_G = zeros([gridsize,n_fin_vert])
B_Gx = B_G
B_Gz_vert = B_G

for i=1:n_fin_vert
    Beta = (z-Z0_fin_vert(i)).^2 + (x-X0_fin_vert(i)).^2
    const_G(i)=mu.*I_Guide(i)./(4*pi)
    B_G(:,:,i)=const_G(i).*((y-YD(i))./(Beta.*sqrt(Beta+...
        (y-YD(i)).^2))-(y-YU(i))./(Beta.*sqrt(Beta+(y-YU(i)).^2)))
    B_Gx(:,:,i)=B_G(:,:,i).*(z-Z0_fin_vert(i))
    B_Gz_vert(:,:,i)=B_G(:,:,i).*(X0_fin_vert(i)-x)
end

## Finite Normal Wires

#unpack parameters
ZD = fin_norm_params(1,:)
ZU = fin_norm_params(2,:)
X0 = fin_norm_params(3,:)
Y0 = fin_norm_params(4,:)
I = fin_norm_params(5,:)

n_fin_norm = size(fin_norm_params)n_fin_norm = n_fin_norm(2)

#preallocate resources
const_G = zeros(size(I))
B_G = zeros([gridsize,n_fin_norm])
B_Gx_norm = B_G
B_Gy_norm = B_G

for i=1:n_fin_norm
    Beta = (x-X0(i)).^2 + (y-Y0(i)).^2
    const_G(i)=mu.*I(i)./(4*pi)
    B_G(:,:,i)=const_G(i).*((z-ZD(i))./(Beta.*sqrt(Beta+...
        (z-ZD(i)).^2))-(z-ZU(i))./(Beta.*sqrt(Beta+(z-ZU(i)).^2)))
    B_Gx_norm(:,:,i)=B_G(:,:,i).*(Y0(i)-y)
    B_Gy_norm(:,:,i)=B_G(:,:,i).*(x-X0(i))
end

# ## 1/2 infinite Vertical Wires
# 
# #unpack parameters
# X0_half_fin_vert = half_fin_vert_params(1,:)
# Y0_half_fin_vert = half_fin_vert_params(2,:)
# Z0_half_fin_vert = half_fin_vert_params(3,:)
# dir_vert = half_fin_vert_params(4,:)
# I_GateU = half_fin_vert_params(5,:)
# 
# n_half_fin_vert = size(half_fin_vert_params) n_half_fin_vert = n_half_fin_vert(2)
# 
# #preallocate resources
# const_GateU = zeros(size(I_GateU))
# A = zeros([gridsize,n_half_fin_vert])
# Alpha = A
# Y = A
# B_GateU = A
# B_GateUx = A
# B_GateUz_vert = A
# 
# for i=1:n_half_fin_vert
#     A(:,:,i)=x-X0_half_fin_vert(i)
#     Alpha(:,:,i)=sqrt(A(:,:,i).^2+(z-Z0_half_fin_vert(i)).^2+(y-Y0_half_fin_vert(i)).^2)
#     Y(:,:,i)=1 + dir_vert(i)*(y-Y0_half_fin_vert(i))./Alpha(:,:,i)
#     const_GateU(i)=mu.*I_GateU(i)./(4*pi)
#     B_GateU(:,:,i)=const_GateU(i).*(Y(:,:,i)./(A(:,:,i).^2+(z-Z0_half_fin_vert(i)).^2))
#     B_GateUx(:,:,i)=B_GateU(:,:,i).*(z-Z0_half_fin_vert(i))
#     B_GateUz_vert(:,:,i)=-B_GateU(:,:,i).*A(:,:,i)
# end

# ## 1/2 - infinite Horizontal Wires
# #unpack parameters
# #first row is x_0
# #second row is z_0
# #third row is direction (+1 is right, -1 is left)
# #fourth row is I
# X0_half_fin_horz = half_fin_horz_params(1,:)
# Y0_half_fin_horz = half_fin_horz_params(2,:)
# Z0_half_fin_horz = half_fin_horz_params(3,:)
# dir_horz = half_fin_horz_params(4,:)
# I_GateU = half_fin_horz_params(5,:)
# 
# n_half_fin_horz = size(half_fin_horz_params)n_half_fin_horz = n_half_fin_horz(2)
# 
# #preallocate resources
# const_GateU = zeros(size(I_GateU))
# B = zeros([gridsize,n_half_fin_horz])
# Beta = B
# X = B
# B_GateU = B
# B_GateUy = B
# B_GateUz_horz = B
# 
# for i=1:n_half_fin_horz
#     B(:,:,i)=y-Y0_half_fin_horz(i)
#     Beta(:,:,i)=sqrt(B(:,:,i).^2+(z-Z0_half_fin_horz(i)).^2+(x-X0_half_fin_horz(i)).^2)
#     X(:,:,i)=1 + dir_horz(i)*(x-X0_half_fin_horz(i))./Beta(:,:,i)
#     const_GateU(i)=mu.*I_GateU(i)./(4*pi)
#     B_GateU(:,:,i)=const_GateU(i).*(X(:,:,i)./(B(:,:,i).^2+(z-Z0_half_fin_horz(i)).^2))
#     B_GateUy(:,:,i)=B_GateU(:,:,i).*(Z0_half_fin_horz(i)-z)
#     B_GateUz_horz(:,:,i)=B_GateU(:,:,i).*B(:,:,i)
# end

## 1/2 - infinite Normal Wires
# 
# #DANGER! Polarity not corrected
# 
# #unpack parameters
# 
# X0_half_fin_norm = half_fin_norm_params(1,:)
# Y0_half_fin_norm = half_fin_norm_params(2,:)
# dir_norm = half_fin_norm_params(3,:)
# I_Norm = half_fin_norm_params(4,:)
# 
# n_half_fin_norm = size(half_fin_norm_params)n_half_fin_norm = n_half_fin_norm(2)
# 
# #preallocate resources
# const_Norm = zeros(size(I_Norm))
# X = zeros([gridsize,n_half_fin_vert])
# Y = X
# Z = X
# Beta = X
# B_Norm = X
# B_Normx = X
# B_Normy = X
# 
# for i=1:n_half_fin_norm
#     X(:,:,i)=x-X0_half_fin_norm(i)
#     Y(:,:,i)=y-Y0_half_fin_norm(i)
#     Beta(:,:,i)=sqrt(Y(:,:,i).^2+z.^2+X(:,:,i).^2)
#     Z(:,:,i)=z./Beta(:,:,i) + dir_norm(i)
#     const_Norm(i)=mu.*I_Norm(i)./(4*pi)
#     B_Norm(:,:,i)=const_Norm(i).*(Z(:,:,i)./(X(:,:,i).^2+Y(:,:,i).^2))
#     B_Normx(:,:,i)=B_Norm(:,:,i).*Y(:,:,i)
#     B_Normy(:,:,i)=B_Norm(:,:,i).*-X(:,:,i)
# end
## Field Summation

B_Gy_tot=sum(B_Gy,3)+sum(B_Gy_norm,3)
B_Gz_tot=sum(B_Gz_horz,3)+sum(B_Gz_vert,3)
B_Gx_tot=sum(B_Gx,3)+sum(B_Gx_norm,3)
# B_GateUx_tot=sum(B_GateUx,3)
# B_GateUz_tot=sum(B_GateUz_vert,3)+sum(B_GateUz_horz,3)
# B_GateUy_tot=sum(B_GateUy,3)
# B_Gx_norm_tot=sum(B_Gx_norm,3)
# B_Gy_norm_tot=sum(B_Gy_norm,3)

# B_tot=sqrt((B_Gx_tot + B_GateUx_tot + B_Normx_tot + B_xbias).^2+(B_Gz_tot+B_GateUz_tot+...
#     +B_zbias).^2+(B_Gy_tot+B_GateUy_tot + B_Normy_tot + B_ybias).^2)
# B_tot=sqrt((B_Gx_tot + B_GateUx_tot + B_xbias).^2+(B_Gz_tot+B_GateUz_tot+...
#     +B_zbias).^2+(B_Gy_tot+B_GateUy_tot + B_ybias).^2)
B_tot=sqrt((B_Gx_tot + B_xbias).^2+(B_Gz_tot...
    +B_zbias).^2+(B_Gy_tot+ B_ybias).^2)