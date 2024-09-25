import FWCore.ParameterSet.Config as cms

def CosmicMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('CosmicMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
