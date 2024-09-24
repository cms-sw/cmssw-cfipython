import FWCore.ParameterSet.Config as cms

def CosmicClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('CosmicClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
