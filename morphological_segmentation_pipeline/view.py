import subprocess
import argparse


path='/Volumes/Studies-1/LEGmuscle/Analysis/'
sub='MSTHIGH_06_Jack/'
list = ['FU4']
# list = ['FU','FU2','FU3','FU4']
leg='right'

base = ['fslview', path + sub + 'BL/final/' +'BL_' + leg + '.nii.gz', path + sub + 'BL/final/' + 'BL_'+ leg + '_mask.nii.gz']

for l in list:
    # base.append('fslivew')
    base.append(path + sub + l + '/final/' + l + '_' + leg + '.nii.gz')
    # base.append('fslview')
    base.append(path + sub + l + '/final/' + l + '_' + leg + '_mask.nii.gz')

print(base)
subprocess.call(base)
# if len(list) == 2:
#     subprocess.call(['fslview', path + sub + 'BL/Analysis/' +'BL_' + leg + '.nii.gz', path + sub + list[0] + '/Analysis/' + list[0] + '_' + leg + '_ref2bl.nii.gz', path + sub +  list[1] + '/Analysis/' + list[1] + '_' + leg + '_ref2bl.nii.gz'])
# # fslview $full$'BL/BL_'$leg$'.nii.gz' $full${l[0]}$'/'${l[0]}$'_'$leg$'_ref2bl.nii.gz'
# else:
#     subprocess.call(['fslview', path + sub + 'BL/Analysis/' +'BL_' + leg + '.nii.gz', path + sub + list[0] + '/Analysis/' + list[0] + '_' + leg + '_ref2bl.nii.gz', path + sub +  list[1] + '/Analysis/' + list[1] + '_' + leg + '_ref2bl.nii.gz', path + sub + list[2] + '/Analysis/' + list[2] + '_' + leg + '_ref2bl.nii.gz', path + sub + list[3] + '/Analysis/' + list[3] + '_' + leg + '_ref2bl.nii.gz'])
     