import FWCore.ParameterSet.Config as cms

def DTT0Calibration(**kwargs):
  mod = cms.EDAnalyzer('DTT0Calibration',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
