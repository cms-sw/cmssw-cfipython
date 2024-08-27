import FWCore.ParameterSet.Config as cms

def RPCPointVsRecHit(**kwargs):
  mod = cms.EDProducer('RPCPointVsRecHit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
