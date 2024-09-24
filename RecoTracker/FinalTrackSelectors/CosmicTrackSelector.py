import FWCore.ParameterSet.Config as cms

def CosmicTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('CosmicTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
