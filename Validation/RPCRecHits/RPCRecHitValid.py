import FWCore.ParameterSet.Config as cms

def RPCRecHitValid(**kwargs):
  mod = cms.EDProducer('RPCRecHitValid',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
