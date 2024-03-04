import FWCore.ParameterSet.Config as cms

def CosmicMuonSeedGenerator(**kwargs):
  mod = cms.EDProducer('CosmicMuonSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
