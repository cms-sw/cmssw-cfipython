import FWCore.ParameterSet.Config as cms

def PFRecHitProducer(**kwargs):
  mod = cms.EDProducer('PFRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
