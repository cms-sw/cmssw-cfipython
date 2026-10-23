import FWCore.ParameterSet.Config as cms

def MuonShallowCloneProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonShallowCloneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
