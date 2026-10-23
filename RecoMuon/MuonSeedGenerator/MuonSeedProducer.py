import FWCore.ParameterSet.Config as cms

def MuonSeedProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonSeedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
