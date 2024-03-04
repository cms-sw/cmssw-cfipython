import FWCore.ParameterSet.Config as cms

def CosmicMuonLinksProducer(**kwargs):
  mod = cms.EDProducer('CosmicMuonLinksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
