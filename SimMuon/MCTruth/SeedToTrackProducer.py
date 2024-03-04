import FWCore.ParameterSet.Config as cms

def SeedToTrackProducer(**kwargs):
  mod = cms.EDProducer('SeedToTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
