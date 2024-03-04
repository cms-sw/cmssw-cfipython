import FWCore.ParameterSet.Config as cms

def DTT0CalibrationRMS(**kwargs):
  mod = cms.EDAnalyzer('DTT0CalibrationRMS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
