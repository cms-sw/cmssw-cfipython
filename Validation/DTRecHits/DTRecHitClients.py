import FWCore.ParameterSet.Config as cms

def DTRecHitClients(**kwargs):
  mod = cms.EDProducer('DTRecHitClients',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
