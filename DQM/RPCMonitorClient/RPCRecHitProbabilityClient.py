import FWCore.ParameterSet.Config as cms

def RPCRecHitProbabilityClient(**kwargs):
  mod = cms.EDProducer('RPCRecHitProbabilityClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
