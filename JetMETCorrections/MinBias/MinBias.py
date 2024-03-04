import FWCore.ParameterSet.Config as cms

def MinBias(**kwargs):
  mod = cms.EDAnalyzer('MinBias',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
