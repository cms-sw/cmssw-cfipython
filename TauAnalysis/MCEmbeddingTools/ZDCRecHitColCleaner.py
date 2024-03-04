import FWCore.ParameterSet.Config as cms

def ZDCRecHitColCleaner(**kwargs):
  mod = cms.EDProducer('ZDCRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
