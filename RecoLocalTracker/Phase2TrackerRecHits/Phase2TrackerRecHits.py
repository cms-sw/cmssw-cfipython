import FWCore.ParameterSet.Config as cms

def Phase2TrackerRecHits(*args, **kwargs):
  mod = cms.EDProducer('Phase2TrackerRecHits',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
