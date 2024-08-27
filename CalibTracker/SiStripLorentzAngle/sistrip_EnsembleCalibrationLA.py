import FWCore.ParameterSet.Config as cms

def sistrip_EnsembleCalibrationLA(**kwargs):
  mod = cms.EDAnalyzer('sistrip::EnsembleCalibrationLA',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
