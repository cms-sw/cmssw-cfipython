import FWCore.ParameterSet.Config as cms

def MCMuonSeedGenerator2(*args, **kwargs):
  mod = cms.EDProducer('MCMuonSeedGenerator2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
