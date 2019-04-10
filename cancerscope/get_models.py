"""
Setup file for models required by SCOPE
"""
from config import SCOPEMODELS_DATADIR, SCOPEMODELS_LIST, SCOPEMODELS_FILELIST_DIR
import cancerscope
import os, sys
import tempfile
import shutil, six
## Get detailed list of models and source files
modelOptions = {}
with open(SCOPEMODELS_LIST, 'r') as f:
	for line in f:
		if line.strip()!= '':
			modelname, url, expectedFile, expectedmd5 = line.strip().split('\t')
			modelOptions[modelname] = (url, expectedFile, expectedmd5)

def findmodel(expected_pckgdir, model_label, expected_targetdir=None):
	expectedFilename = "model_" + model_label + ".txt"
	modelOptions_local = {}
	"""First check if the model details file exists in the main cancerscope directory (proof that model download attempt was completed atleast"""
	if os.path.exists(expected_pckgdir + "/" + expectedFilename):
		with open(expected_pckgdir + "/" + expectedFilename) as f:
			sys.stdout.write("Reading model url and naming criterion")
			for line in f:
				if line.strip()!= '':
					modelname_, url_, modeldir = line.strip().split('\t')
					modelOptions_local[modelname_] = modeldir + "/" + model_label.split("_")[-1]
	
	else:
		"""Otherwise, it would appear model wasnt even attempted to be downloaded"""
		if expected_targetdir is not None:
			sys.stdout.write("Model file {0} proceeding with download...".format(model_label))
			dnld_dir = downloadmodel(model_label = model_label, targetdir=expected_targetdir)
			modelOptions_local[model_label] = dnld_dir + "/" + model_label.split("_")[-1]
		else:
			sys.stdout.write("Expected model directory {0} does not exist".format(expected_targetdir))
			return None
	
	if bool(modelOptions_local) is True:
		if os.path.exists(modelOptions_local[model_label] + "/lasagne_bestparams.npz") is True:
			sys.stdout.write("Model file found, returning to user")
			return modelOptions_local
		else:
			if not os.path.exists(modelOptions_local[model_label]):
				"""The model directory does not exist in cancerscope/data, so need to re-download"""
				sys.stdout.write("Model download directory does not exist")
				if expected_targetdir is not None:
					sys.stdout.write("Downloading model {0}".format(model_label))
					dnld_dir = downloadmodel(model_label = model_label, targetdir=expected_targetdir)
					modelOptions_local[model_label] = dnld_dir + "/" + model_label.split("_")[-1]
				else:
					sys.stdout.write("Model directory does not exist, but no target directory provided in case of missing model files. Return None")
					return None
	else:
		sys.stdout.write("No model details file found")
		return None
	
def getmodel(model_label=None):
	"""Base function to retrieve models downloaded to package site directory"""
	model_dirs = {}
	if model_label is None:
		for m, _ in modelOptions.items():
			m_dirtemp = findmodel(expected_pckgdir = SCOPEMODELS_FILELIST_DIR, model_label = m, expected_targetdir = SCOPEMODELS_DATADIR)
			if m_dirtemp is not None:
				model_dirs[m] = m_dirtemp
			else:
				m_dirtemp = findmodel(expectedDir = expectedDir, model_label = model_label)
	else:
		m_dirtemp = findmodel(expectedDir = expectedDir, model_label = model_label)
		model_dirs[model_label] = m_dirtemp
	return model_dirs

def downloadmodel(model_label=None, targetdir=None):
	"""
	Query Zenodo and retrieve version-specific model parameter files and metadata
	"""
	global modelOptions
	
	if targetdir is not None:
		tempDir = targetdir
	else:
		tempDir = SCOPEMODELS_DATADIR ## By default, download models to the cancerscope/data directory, not tempfile.mkdtemp()
	
	if model_label is None:
		for m, _ in modelOptions.items():
			downloadmodel(m, tempDir)
	else:
		assert model_label in modelOptions.keys(), "%s is not a valid option in %s" % (model_label, modelOptions.keys())
		sys.stdout.write("Downloading model files for {0} \n\tData Downloaded at: {1}".format(model_label, tempDir))
		url, expectedFile, expectedmd5 = modelOptions[model_label]
		filesToDownload = [(url, expectedFile, expectedmd5)]
		expectedDir = expectedFile.replace(".tar.gz", "")
	
		try:
			cancerscope.utils._downloadFiles(filesToDownload, tempDir)
		except Exception as e:
			print(e)
			exc_info = sys.exc_info(); shutil.rmtree(tempDir); six.reraise(*exc_info)
	
		mainDir = os.path.abspath(tempDir)
		with open(SCOPEMODELS_FILELIST_DIR + "/model_" + model_label + ".txt", "w") as f:
			f.write("\t".join([model_label, url, mainDir]))
		return(mainDir)

