import FWCore.ParameterSet.Config as cms

def DTT0Correction(**kwargs):
  mod = cms.EDAnalyzer('DTT0Correction',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
