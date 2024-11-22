import FWCore.ParameterSet.Config as cms

def PFClusterMETProducer(*args, **kwargs):
  mod = cms.EDProducer('PFClusterMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
