import FWCore.ParameterSet.Config as cms

def L3MuonTrajectorySeedCombiner(*args, **kwargs):
  mod = cms.EDProducer('L3MuonTrajectorySeedCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
