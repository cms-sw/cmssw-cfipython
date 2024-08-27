import FWCore.ParameterSet.Config as cms

def RPCRecHitReader(**kwargs):
  mod = cms.EDAnalyzer('RPCRecHitReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
