import FWCore.ParameterSet.Config as cms

def CosmicTrackSplitter(**kwargs):
  mod = cms.EDProducer('CosmicTrackSplitter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
