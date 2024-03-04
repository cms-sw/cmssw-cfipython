import FWCore.ParameterSet.Config as cms

def CastorRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('CastorRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
