import FWCore.ParameterSet.Config as cms

def OutsideInMuonSeeder(**kwargs):
  mod = cms.EDProducer('OutsideInMuonSeeder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
