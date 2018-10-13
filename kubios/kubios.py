# -*- coding: utf-8 -*-
"""
Kubios Import & Export
----------------------

This module provides functions to export NN/RR interval series in KUBIOS readable formats and import KUBIOS HRV results
from KUBIOS report files in .TXT format.

Notes
-----
..  This module is part of the master thesis
	"Development of an Open-Source Python Toolbox for Heart Rate Variability (HRV)".

Author
------
..  Pedro Gomes, Master Student, University of Applied Sciences Hamburg

Thesis Supervisors
------------------
..  Hugo Silva, PhD, Instituto de Telecomunicacoes, PLUX wireless biosignals S.A.
..  Prof. Dr. Petra Margaritoff, University of Applied Sciences Hamburg

Last Update
-----------
13-09-2018

:copyright: (c) 2018 by Pedro Gomes
:license: BSD 3-clause, see LICENSE for more details.
"""
# Imports
import json
import os
import datetime as dt


def export_nni(series=None, output_path=None, output_file=None, info=None):
	"""Exports NN or RR interval series into a KUBIOS readable file in *.TXT format.

	Parameters
	----------
	series : array_like
		ECG signal or NN/RR interval series in (s) or (ms).
	output_path : str, optional
		Absolute path to where the export files should be stored (alternatively add it directly to the 'output_file')
	output_file : str
		Name of the exported file.
	info : dict, optional
		Dictionary with information about the ECG acquisition.
		Keys:	'file'					File name of the original ECG acquisition.
				'device'				Device used for acquisition.
				'deviceID'				Device ID (e.g. MAC address)
				'sampling rate'			Sampling rate used for acquisition.
				'sampling resolution' 	Sampling resolution used for acquisition.
				'comment'				String comment(s).

	Raises
	------
	TypeError
		If input data is provided.
	"""
	# Check input
	if series is None:
		raise TypeError("No input data ('nni') provided. Please specify input data.")

	# Output file name generation
	if output_file is None:
		output_file = '/series_export' + dt.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
	elif output_file[-4:] != '.txt':
		output_file += '.txt'

	if output_path is not None:
		output_file = output_path + output_file

	# Information file
	if info is None:
		info = dict()

	info['file'] = str(info['file']) if 'file' in info.keys() else 'n/a'
	info['device'] = str(info['device'])if 'device' in info.keys() else 'n/a'
	info['deviceID'] = str(info['deviceID']) if 'deviceID' in info.keys() else 'n/a'
	info['sampling_rate'] = str(info['sampling_rate']) if 'sampling_rate' in info.keys() else 'n/a'
	info['sampling_resolution'] = str(info['sampling_resolution']) if 'sampling_resolution' in info.keys() else 'n/a'
	info['comment'] = str(info['comment']) if 'comment' in info.keys() else 'n/a'

	vals = (info['file'], info['device'], info['deviceID'], info['sampling_rate'], info['sampling_resolution'],
			info['comment'])

	header = '# SIGNAL/SERIES EXPORT - KUBIOS\n' \
			 '# File:				%s\n' \
			 '# Device:	 			%s\n' \
			 '# DeviceID / MAC: 	%s\n' \
			 '# Sampling rate: 		%s\n' \
			 '# Resolution:			%s\n' \
			 '# Comment:			%s\n' % vals

	# Output data
	with open(output_file, 'w+') as f:
		f.write(header)
		for i in series:
			f.write('%.3f\n' % i)


def import_report(rfile=None, delimiter=','):
	"""Imports HRV results from a KUBIOS report file in .txt format.

	Parameters
	----------
	rfile : str, file handler
		Absolute filepath or file handler of the KUBIOS report file.
	delimiter : str, character
		Delimiter used in KUBIOS report file.

	Returns
	-------
	results : dict
		Imported parameter values from the KUBIOS report file.

	Raises
	------
	TypeError
		If 'rfile' is not str or file handler.
	IOError
		If provided file does not exist.
	TypeError
		If 'rfile' is not a KUBIOS report file.
	"""
	# Check input
	if type(rfile) is not str and type(rfile) is not file:
		raise TypeError('Unsupported file format. Please provide file path (str) or file handler.')
	elif type(rfile) is str:
		if not os.path.isfile(rfile):
			raise IOError('KUBIOS report file does not exist. Please verify input data.')

	# Check if file is a Kubios export file
	with open(rfile, 'r') as f:
		if 'Kubios HRV' not in f.read():
			raise TypeError("This file does not seem to be a KUBIOS report file.")

	# Load HRV keys
	dir_ = os.path.split(__file__)
	with open(os.path.join(dir_[0], 'keys.json')) as j:
		hrv_parameters = json.load(j)

	# Get non-available parameters
	results = {}
	frequency_arrays = ['fft_peak', 'fft_abs', 'fft_log', 'fft_rel', 'fft_norm', 'ar_peak', 'ar_abs', 'ar_log',
						'ar_norm', 'ar_rel']

	for key in hrv_parameters.keys():
		if 'fft_' in key or 'ar_' in key:
			if key in frequency_arrays:
				results[str(key)] = list()

	# Get available parameters
	with open(rfile, 'r') as f:
		content = f.readlines()

	# Get data
	for line in content:
		line = line.split(delimiter)
		for key, label in hrv_parameters.items():
			if type(label) is unicode:
				if str(label) in line[0]:
					index = 2 if key in ['ar_total', 'ar_ratio'] else (1 if len(line) > 1 else 0)
					try:
						val = float(line[index].lstrip())
					except ValueError:
						val = str(line[index]).rstrip().lstrip().replace('\n', '').replace('\r', '')
						if key in ['interpolation', 'ar_model', 'fft_window', 'fft_overlap', 'fft_grid', 'threshold']:
							val = float(''.join(i for i in val if i.isdigit()))
					results[str(key)] = val if not line[index].isspace() else 'n/a'
			else:
				for l in label:
					if str(l) == line[0].rstrip().lstrip().replace(':', ''):
						index = 1 if 'fft_' in key else 2
						val = float(line[index].lstrip()) if not line[index].isspace() else 'n/a'
						results[str(key)].append(val)
	return results

if __name__ == "__main__":
	"""
	Example Script - Kubios Package
	"""
	import numpy as np

	# Get a NNI series (alternatively ECG data)
	nni = np.load('SampleSeries.npy')

	# Create info dictionary (optional)
	info = {
		'file': 'RandomSamples',
		'device': 'n/a',
		'deviceID': 'n/a',
		'sampling_rate': 'n/a',
		'sampling_resolution': 'n/A',
		'comment': 'These are the RR intervals of the SampleSeries.'
	}

	# Create Kubios readable file with imported data (ECG, RR, or NN)
	export_nni(nni, output_file='SampleExport.txt', info=info)

	# Load Sample Kubios Report
	results = import_report('SampleReport.txt')

	for key in results.keys():
		print(key, results[key])
