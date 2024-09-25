import FWCore.ParameterSet.Config as cms

def RPCPointVsRecHit(*args, **kwargs):
  mod = cms.EDProducer('RPCPointVsRecHit',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
