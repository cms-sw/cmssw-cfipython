import FWCore.ParameterSet.Config as cms

def MuonSeedTrack(**kwargs):
  mod = cms.EDProducer('MuonSeedTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
