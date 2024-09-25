import FWCore.ParameterSet.Config as cms

def ClusterMCsplitStrips(*args, **kwargs):
  mod = cms.EDProducer('ClusterMCsplitStrips',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
