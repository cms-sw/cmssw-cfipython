import FWCore.ParameterSet.Config as cms

def DTT0CalibrationRMS(*args, **kwargs):
  mod = cms.EDAnalyzer('DTT0CalibrationRMS',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
