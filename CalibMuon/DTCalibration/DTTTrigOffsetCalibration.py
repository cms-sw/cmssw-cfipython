import FWCore.ParameterSet.Config as cms

def DTTTrigOffsetCalibration(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigOffsetCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
