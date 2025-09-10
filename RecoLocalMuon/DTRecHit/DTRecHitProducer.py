import FWCore.ParameterSet.Config as cms

def DTRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('DTRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
