import FWCore.ParameterSet.Config as cms

def GlobalCosmicMuonProducer(**kwargs):
  mod = cms.EDProducer('GlobalCosmicMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
