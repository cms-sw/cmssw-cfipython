import FWCore.ParameterSet.Config as cms

def HBHERecHitColCleaner(*args, **kwargs):
  mod = cms.EDProducer('HBHERecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
