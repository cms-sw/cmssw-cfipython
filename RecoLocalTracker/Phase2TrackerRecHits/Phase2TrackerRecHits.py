import FWCore.ParameterSet.Config as cms

def Phase2TrackerRecHits(**kwargs):
  mod = cms.EDProducer('Phase2TrackerRecHits',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
