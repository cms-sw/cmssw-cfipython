import FWCore.ParameterSet.Config as cms

def MuonSeedProducer(**kwargs):
  mod = cms.EDProducer('MuonSeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
