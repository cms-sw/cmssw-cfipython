import FWCore.ParameterSet.Config as cms

def HGC3DClusterGenMatchSelector(*args, **kwargs):
  mod = cms.EDProducer('HGC3DClusterGenMatchSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
