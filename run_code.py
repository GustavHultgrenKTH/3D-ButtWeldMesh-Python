#import os, buttweld3d
import os, weld3d

base = r"C:\Users\gusta\OneDrive - KTH\00_GitHub\ButtWeld-3D\04_Test_Python"
param_file = os.path.join(base, "mesh_parameter.txt")
weld_file  = os.path.join(base, "C2-2_D12_cs_cleaned.pcd")  # or .mat

#bw = buttweld3d.initialize()
fw = weld3d.initialize()
try:
    inputFile = fw.weld_3D(param_file, weld_file, "C2-2_D12_cs_cleaned", nargout=1)
    print("inputFile:", inputFile)
    #print("nodeFile:", nodeFile)
    #print("elemFile:", elemFile)
finally:
    try: fw.terminate()
    except Exception: pass