import FWCore.ParameterSet.Config as cms

def HORecHitColCleaner(**kwargs):
  mod = cms.EDProducer('HORecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
