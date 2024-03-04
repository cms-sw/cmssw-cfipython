import FWCore.ParameterSet.Config as cms

def RPCRecHitProducer(**kwargs):
  mod = cms.EDProducer('RPCRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
