import FWCore.ParameterSet.Config as cms

def L2MuonSeedGenerator(**kwargs):
  mod = cms.EDProducer('L2MuonSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
