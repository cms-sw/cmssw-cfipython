import FWCore.ParameterSet.Config as cms

def SETMuonSeedProducer(**kwargs):
  mod = cms.EDProducer('SETMuonSeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
