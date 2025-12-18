import FWCore.ParameterSet.Config as cms

def TrackingRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackingRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
