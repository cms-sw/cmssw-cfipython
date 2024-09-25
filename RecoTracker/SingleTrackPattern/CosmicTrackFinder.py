import FWCore.ParameterSet.Config as cms

def CosmicTrackFinder(*args, **kwargs):
  mod = cms.EDProducer('CosmicTrackFinder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
