import os, buttweld3d

base = r"C:\Users\gusta\OneDrive - KTH\00_GitHub\ButtWeld-3D\04_Test_Python"
param_file = os.path.join(base, "buttweld_params_template.txt")
weld_file  = os.path.join(base, "specimen02.pcd")  # or .mat

bw = buttweld3d.initialize()
try:
    inputFile = bw.fun_buttweld_3D(param_file, weld_file, "specimen02", nargout=1)
    print("inputFile:", inputFile)
    #print("nodeFile:", nodeFile)
    #print("elemFile:", elemFile)
finally:
    try: bw.terminate()
    except Exception: pass