import FWCore.ParameterSet.Config as cms

def CosmicMuonProducer(**kwargs):
  mod = cms.EDProducer('CosmicMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
