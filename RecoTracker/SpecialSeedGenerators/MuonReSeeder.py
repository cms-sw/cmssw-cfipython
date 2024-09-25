import FWCore.ParameterSet.Config as cms

def MuonReSeeder(*args, **kwargs):
  mod = cms.EDProducer('MuonReSeeder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
