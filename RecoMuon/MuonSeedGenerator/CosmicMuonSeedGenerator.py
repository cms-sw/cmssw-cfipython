import FWCore.ParameterSet.Config as cms

def CosmicMuonSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('CosmicMuonSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
