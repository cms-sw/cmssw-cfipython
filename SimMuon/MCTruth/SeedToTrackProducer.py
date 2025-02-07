import FWCore.ParameterSet.Config as cms

def SeedToTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('SeedToTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
