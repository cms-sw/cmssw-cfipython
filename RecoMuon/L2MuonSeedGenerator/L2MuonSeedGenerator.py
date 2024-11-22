import FWCore.ParameterSet.Config as cms

def L2MuonSeedGenerator(*args, **kwargs):
  mod = cms.EDProducer('L2MuonSeedGenerator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
