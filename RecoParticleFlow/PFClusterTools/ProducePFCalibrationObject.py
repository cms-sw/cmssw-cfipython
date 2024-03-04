import FWCore.ParameterSet.Config as cms

def ProducePFCalibrationObject(**kwargs):
  mod = cms.EDAnalyzer('ProducePFCalibrationObject',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
