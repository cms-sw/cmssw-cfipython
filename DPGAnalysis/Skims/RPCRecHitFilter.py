import FWCore.ParameterSet.Config as cms

def RPCRecHitFilter(**kwargs):
  mod = cms.EDFilter('RPCRecHitFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
