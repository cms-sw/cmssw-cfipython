import FWCore.ParameterSet.Config as cms

def DTRecHitColCleaner(*args, **kwargs):
  mod = cms.EDProducer('DTRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
