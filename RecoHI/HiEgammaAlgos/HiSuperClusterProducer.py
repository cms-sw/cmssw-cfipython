import FWCore.ParameterSet.Config as cms

def HiSuperClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('HiSuperClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
