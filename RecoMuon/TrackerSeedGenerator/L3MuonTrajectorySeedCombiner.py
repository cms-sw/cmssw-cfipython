import FWCore.ParameterSet.Config as cms

def L3MuonTrajectorySeedCombiner(**kwargs):
  mod = cms.EDProducer('L3MuonTrajectorySeedCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
