import FWCore.ParameterSet.Config as cms

def ElectronCalibrationUniv(**kwargs):
  mod = cms.EDAnalyzer('ElectronCalibrationUniv',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
