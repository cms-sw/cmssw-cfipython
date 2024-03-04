import FWCore.ParameterSet.Config as cms

def XMLCalibrationTest(**kwargs):
  mod = cms.EDAnalyzer('XMLCalibrationTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
