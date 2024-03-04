import FWCore.ParameterSet.Config as cms

def MCMuonSeedGenerator2(**kwargs):
  mod = cms.EDProducer('MCMuonSeedGenerator2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
