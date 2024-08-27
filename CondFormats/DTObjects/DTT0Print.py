import FWCore.ParameterSet.Config as cms

def DTT0Print(**kwargs):
  mod = cms.EDAnalyzer('DTT0Print',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
