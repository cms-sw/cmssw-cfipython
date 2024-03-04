import FWCore.ParameterSet.Config as cms

def FastTrackerRecHitCombiner(**kwargs):
  mod = cms.EDProducer('FastTrackerRecHitCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
