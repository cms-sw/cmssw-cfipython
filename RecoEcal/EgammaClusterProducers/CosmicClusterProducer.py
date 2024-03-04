import FWCore.ParameterSet.Config as cms

def CosmicClusterProducer(**kwargs):
  mod = cms.EDProducer('CosmicClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
