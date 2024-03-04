import FWCore.ParameterSet.Config as cms

def BJetEnergyRegressionMVA(**kwargs):
  mod = cms.EDProducer('BJetEnergyRegressionMVA',
    src = cms.required.InputTag,
    variablesOrder = cms.required.vstring,
    name = cms.required.string,
    isClassifier = cms.required.bool,
    variables = cms.PSet(),
    weightFile = cms.required.FileInPath,
    backend = cms.string('TMVA'),
    inputTensorName = cms.string(''),
    outputTensorName = cms.string(''),
    outputNames = cms.vstring(),
    outputFormulas = cms.vstring(),
    batch_eval = cms.bool(False),
    disableONNXGraphOpt = cms.bool(False),
    pvsrc = cms.required.InputTag,
    svsrc = cms.required.InputTag,
    rhosrc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
