import FWCore.ParameterSet.Config as cms

def RPCRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('RPCRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
