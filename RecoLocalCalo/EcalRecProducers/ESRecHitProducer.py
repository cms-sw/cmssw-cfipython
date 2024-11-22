import FWCore.ParameterSet.Config as cms

def ESRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('ESRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
