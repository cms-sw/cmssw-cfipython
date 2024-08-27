import FWCore.ParameterSet.Config as cms

def CosmicsMuonIdProducer(**kwargs):
  mod = cms.EDProducer('CosmicsMuonIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
