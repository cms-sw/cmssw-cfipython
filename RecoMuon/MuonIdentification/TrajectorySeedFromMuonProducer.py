import FWCore.ParameterSet.Config as cms

def TrajectorySeedFromMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('TrajectorySeedFromMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
