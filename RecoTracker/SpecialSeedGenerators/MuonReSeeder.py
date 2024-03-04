import FWCore.ParameterSet.Config as cms

def MuonReSeeder(**kwargs):
  mod = cms.EDProducer('MuonReSeeder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
