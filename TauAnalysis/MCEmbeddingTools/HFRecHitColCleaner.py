import FWCore.ParameterSet.Config as cms

def HFRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('HFRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
