import FWCore.ParameterSet.Config as cms

def CosmicTrackFinder(**kwargs):
  mod = cms.EDProducer('CosmicTrackFinder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
