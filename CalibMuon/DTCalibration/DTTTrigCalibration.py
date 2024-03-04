import FWCore.ParameterSet.Config as cms

def DTTTrigCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
