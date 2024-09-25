import FWCore.ParameterSet.Config as cms

def DTVDriftCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('DTVDriftCalibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
