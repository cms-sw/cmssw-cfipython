import FWCore.ParameterSet.Config as cms

def CosmicSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('CosmicSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
