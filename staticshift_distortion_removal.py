# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 09:53:37 2018

@author: Kanda-PC
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 23:11:23 2018

@author: Kanda-PC
"""
import os
import os.path
import mtpy.core.mt as mt
import mtpy.analysis.staticshift as ss

list_edi_files = []
print('starting')

mydir = r"/home/seismics/ModEM_2023/deteme-15.02.2023/"
mydir_ss = r"/home/seismics/ModEM_2023/deteme-15.02.2023/"
save_path = r"/home/seismics/ModEM_2023/deteme-15.02.2023/"

for n_file in os.listdir(mydir):
     if n_file.endswith(".edi"):
         abs_path = os.path.join(mydir, n_file)
         try:
             ss.remove_static_shift_spatial_filter(abs_path, radius=1000, num_freq=20, freq_skip=4, shift_tol=0.15, plot=False)
         except Exception as e:
             print(e)

            
        
#remove distortion
#for n_file2 in os.listdir(mydir_ss):
#    if n_file2.endswith(".edi"): 
#        abs_path2 = os.path.join(mydir_ss, n_file2)
#        print (abs_path2)

        # rename the filename      print n_file2
  #      dist_fname = n_file2.replace('ss', '20220103')
#        dist_fname = dist_fname.replace ( '_MT', 'MT')
#        print (dist_fname)
        
#        abs_path3 = os.path.join(save_path, dist_fname)
 #       print (abs_path3)
  #      
           
   #     mt_obj = mt.MT(abs_path2)
 #       distortion, new_z = mt_obj.remove_distortion()
#
    #    print (distortion)
     #   mt_obj.write_edi_file(new_fn=abs_path3, new_Z=new_z)


