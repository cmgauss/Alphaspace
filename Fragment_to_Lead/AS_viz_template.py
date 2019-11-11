#AlphaSpace v2.0 - visualization script

import chimera
import sys
import os
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
from chimera import replyobj # for emitting status messages
import glob

pock_dir = 'pocket_communities'

if os.stat(pock_dir + "/protein.pdb").st_size > 0:
    rc("open " + pock_dir + "/protein.pdb")

if os.stat(pock_dir + "/ligand.pdb").st_size > 0:
    rc("open " + pock_dir + "/ligand.pdb")  
    
comm_list = glob.glob(pock_dir + "/community*")
for fx in range(0,len(comm_list)):
    file = pock_dir + "/community_"+str(fx)+".pdb"
    rc("open " + file )
    
models_cnt = 2 + len(comm_list)

rc("background solid white")
rc("windowsize 1200 900")
try:
    rc("~longbond")
except:
    pass

rc("colordef my_teal #00a5a5")
rc("colordef my_gold #e6c200")
rc("colordef my_coregreen #4ea24e")
rc("colordef my_lime #bfff00")
rc("colordef my_peri #7d7fc2")
rc("colordef my_orange #ff821a")
rc("colordef my_dkpurple #8a65a3")
rc("colordef my_ltgreen #7fc27d")
rc("colordef my_coral #FF4040")
rc("colordef my_pink #de7a8e")
rc("colordef my_blue #3973ac")
rc("colordef my_ltblue #71acd6")
rc("colordef my_peach #de987a")
rc("colordef my_rasp #8b0045")
rc("colordef my_foam #7dc2c0")

with open('colors_chimera.txt','r') as f:
    colors = f.read().splitlines()

colors = colors * 20

rc("~display #0-1")

rc("rep stick #0-1")
rc("color white,r,a #0")
rc("color byhet,a #0")
rc("rib #0")

rc("color dimgrey,r,a #1")
rc("color byhet,a #1")
rc("rib #1")
rc("disp #1")


rc("~bond #2-" + str(models_cnt - 1))
rc("rep sphere #2-" + str(models_cnt - 1))
rc("rep bs :BAC")
rc("vdwdefine 1.5 @BAO")

try:
    rc("ribscale 'thin ribbon' #0-1")
except:
    pass

rc("center #1")

rc("surfcat prot_s #0")
rc("color white,s prot_s")

rc("~sel")
rc("surf prot_s")
rc("lighting reflectivity 100")
rc("lighting reflectivity 0")

for i in range(2, models_cnt+1):
    rc("~disp #"+str(i))
    rc("disp #"+str(i)+" & @BAO")
    rc("color my_coregreen :BHI")
    rc("color my_blue :BMI")
    rc("color rosybrown :BLI")

rc("disp #1")
rc("sel #2-"+str(models_cnt+1)+" & #1 z<4.0")
rc("sel up")
rc("~disp ~sel")
rc("transparency 50,a @BAO")
rc("disp #1")

rc("scene 1 save")

rc("~sel")
rc("~surf prot_s")
rc("~disp #2-"+str(models_cnt+1))

rc("disp #1")
rc("defattr "+pock_dir+"/pocket_optimize_attributes.txt")
rc("rangecolor optimize,a 0 gold 50 white 100 forestgreen")
rc("sel #2-"+str(models_cnt+1)+" & #1 z<4.0")
rc("sel up")
rc("disp sel & @BAO")
rc("~sel " )
rc("transparency 50,a @BAO")
rc("scene 2 save")

rc("disp #1")
rc("~disp #2-"+str(models_cnt+1))
rc("defattr "+pock_dir+"/beta_score_attributes.txt")
rc("rangecolor beta_score,a -0.7 forestgreen -0.3 white 0 my_orange")
rc("sel #2-"+str(models_cnt+1)+" & #1 z<4.0")
rc("sel up")
rc("disp sel")
rc("color white,a @BAO")
rc("transparency 70,a @BAO")
rc("~sel " )
rc("scene 3 save")



#
#for i in range(pdb_cnt, models_cnt+1):
#	rc("~display #" + str(i) + " & ~:PAC,AAC,ACC")
#
#rc("color dim grey,a #0")
#rc("color light grey,r #0")
#rc("color byhet,a #0")
#
#rc("surfcat surf_0 #0")
#rc("surface surf_0")
#rc("color white,s #0")
#
#rc("lighting reflectivity 100")
#rc("lighting reflectivity 0")
#
#rc("color rosy brown,s :.L za<0.2 & #0")
#rc("color rosy brown,a :AAC.L")
#rc("color my_blue,s :.M za<0.2 & #0")
#rc("color my_blue,a :AAC.M")
#rc("color my_coregreen,s :.H za<0.2 & #0")
#rc("color forest green,a :AAC.H")
#rc("disp :AAC,ACC")
#
#rc("scene 3 save")
#
#rc("color light grey,s #0")
#rc("~disp :AAC")
#rc("color rosy brown,a :ACC.L")
#rc("color my_blue,a :ACC.M")
#rc("color my_coregreen,a :ACC.H")
#rc("vdwdefine 1.1 :ACC")
#
#rc("scene 4 save")
#
#for i in range(pdb_cnt, models_cnt+1):
#    rc("color " + colors[i-3] +",a #" + str(i) + ":ACC")
#
#rc("scene 5 save")
#
#rc("color white,a :ACC")
#rc("transparency 65,a :ACC")
#rc("vdwdefine 1.3 :ACC")
#
#rc("color white,a @AAO")
#rc("color my_coral,a @AAU")
#rc("sel @AAO")
#rc("sel up")
#rc("color my_lime sel & ~@AAO")
#rc("disp :AAC")
#
#rc("scene 6 save")
#
#rc("color white,s #0")
#
#for i in range(models_cnt, pdb_cnt-1, -1):
##        rc("~surface surf_p" + str(i))
#        rc("sel #" + str(i) + " za<0.2 & #0")
#        rc("color " + colors[i-3] + ",s sel")
#for i in range(pdb_cnt, models_cnt+1):
#    rc("color " + colors[i-3] +",a #" + str(i) + ":AAC")
#    rc("disp :AAC")
#
#rc("scene 7 save")
#
#
#rc("~sel")
#
#