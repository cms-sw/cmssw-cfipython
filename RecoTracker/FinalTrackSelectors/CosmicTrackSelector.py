import FWCore.ParameterSet.Config as cms

def CosmicTrackSelector(**kwargs):
  mod = cms.EDProducer('CosmicTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
