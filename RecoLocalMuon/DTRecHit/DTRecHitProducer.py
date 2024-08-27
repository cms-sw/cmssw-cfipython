import FWCore.ParameterSet.Config as cms

def DTRecHitProducer(**kwargs):
  mod = cms.EDProducer('DTRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
