import FWCore.ParameterSet.Config as cms

def CosmicSeedGenerator(**kwargs):
  mod = cms.EDProducer('CosmicSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
