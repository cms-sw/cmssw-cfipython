import FWCore.ParameterSet.Config as cms

def DTRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('DTRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
