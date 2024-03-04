import FWCore.ParameterSet.Config as cms

def RPCRecHitValidClient(**kwargs):
  mod = cms.EDProducer('RPCRecHitValidClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
