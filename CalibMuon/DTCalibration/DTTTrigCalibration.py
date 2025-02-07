import FWCore.ParameterSet.Config as cms

def DTTTrigCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTTrigCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
