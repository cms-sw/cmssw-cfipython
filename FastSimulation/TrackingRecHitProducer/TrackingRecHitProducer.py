import FWCore.ParameterSet.Config as cms

def TrackingRecHitProducer(**kwargs):
  mod = cms.EDProducer('TrackingRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
