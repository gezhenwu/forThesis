from makeEffCurve import *
import collections
import pickle

#oname    = 'scan_PreCycle_2Feb2022.pkl'
#scan_tag = 'scan_PreCycle_2Feb2022_hv{hv}'
#base_dir = '/home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements'
#meas_dir = 'thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_{q}/pixelOn_{col}_pixelInj_{col}'
#file_name = 'timing_data_dacVth_{dac}_.csv'

#oname    = 'scan_PostCycle_-30_30_7Feb2022.pkl'
#scan_tag = 'scan_PostCycle_-30_30_7Feb2022_hv{hv}'
oname    = 'scan_PostCycle_-30_30_7Feb2022_Meas2.pkl'
scan_tag = 'scan_PostCycle_-30_30_7Feb2022_Meas2_hv{hv}'
base_dir = '/home/makovec/ALTIROC2/cadamuro/FastFadaMeasurements'
meas_dir = 'thresScan/B_22_On_col_Inj_col_N_20_Vth_0_Q_{q}/pixelOn_{col}_pixelInj_{col}'
file_name = 'timing_data_dacVth_{dac}_.csv'

full_name = '/'.join([base_dir, scan_tag, meas_dir, file_name])
collist = ['col{}'.format(i) for i in range(15)]
qlist = [12, 25]

runs = collections.OrderedDict()

scanpoints = list(range(300, 1000)) # points not found are skipped automatically
for hv in ['On', 'Off']:
   runs[hv] = {}
   print('... doing HV', hv)
   for q in qlist:
      print (f'       .. doing q {q}')
      runs[hv][q] = {}
      repl = {'hv' : hv, 'q' : q}
      df = open_scan_series(full_name, collist, scanpoints, other_repl=repl)
      ec = make_curves(df)
      runs[hv][q]['curves'] = ec
      thr = get_thresholds(ec)
      runs[hv][q]['thresholds'] = thr

with open(oname, 'wb') as fout:
    pickle.dump(runs, fout)
