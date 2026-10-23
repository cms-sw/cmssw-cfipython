import FWCore.ParameterSet.Config as cms

def DTTTrigOffsetCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTTrigOffsetCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
