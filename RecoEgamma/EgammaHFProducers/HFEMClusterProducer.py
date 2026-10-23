import FWCore.ParameterSet.Config as cms

def HFEMClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('HFEMClusterProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
