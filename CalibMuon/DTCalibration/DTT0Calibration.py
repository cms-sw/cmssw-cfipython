import FWCore.ParameterSet.Config as cms

def DTT0Calibration(*args, **kwargs):
  mod = cms.EDAnalyzer('DTT0Calibration',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
