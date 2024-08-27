import FWCore.ParameterSet.Config as cms

def RPCRecHitProbability(**kwargs):
  mod = cms.EDProducer('RPCRecHitProbability',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
