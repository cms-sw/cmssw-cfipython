import FWCore.ParameterSet.Config as cms

def ClusterCount(*args, **kwargs):
  mod = cms.EDProducer('ClusterCount',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
