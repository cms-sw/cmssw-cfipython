import FWCore.ParameterSet.Config as cms

def MuonSeedTrack(*args, **kwargs):
  mod = cms.EDProducer('MuonSeedTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
