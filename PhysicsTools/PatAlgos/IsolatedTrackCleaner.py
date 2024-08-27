import FWCore.ParameterSet.Config as cms

def IsolatedTrackCleaner(**kwargs):
  mod = cms.EDProducer('IsolatedTrackCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
