from makeEffCurve import *
import collections 
import pickle

oname    = 'thresh_ThermCycle_restarted_-30_30_3Feb2022_step1To36.pkl'
scan_tag = 'scan_ThermCycle_restarted_-30_30_3Feb2022_step{istep}_hvOn'
base_dir = '/home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements'
meas_dir = 'thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_{q}/pixelOn_{col}_pixelInj_{col}'
file_name = 'timing_data_dacVth_{dac}_.csv'

full_name = '/'.join([base_dir, scan_tag, meas_dir, file_name])
collist = ['col{}'.format(i) for i in range(15)]
qlist = [12, 25]

steplist = list(range(1, 37))
#steplist = [1]

runs = collections.OrderedDict()
scanpoints = list(range(300, 1000)) # points not found are skipped automatically
for istep in steplist:
    print(f'[INFO] analysing step {istep}')
    runs[istep] = {}
    for q in qlist:
        print (f'       .. doing charge {q}')
        runs[istep][q] = {}
        repl = {'istep' : istep, 'q' : q}
        df = open_scan_series(full_name, collist, scanpoints, other_repl=repl)
        ec = make_curves(df)
        runs[istep][q]['curves'] = ec
        thr = get_thresholds(ec)
        runs[istep][q]['thresholds'] = thr

with open(oname, 'wb') as fout:
    pickle.dump(runs, fout)


