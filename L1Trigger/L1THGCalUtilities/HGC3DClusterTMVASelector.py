import FWCore.ParameterSet.Config as cms

def HGC3DClusterTMVASelector(*args, **kwargs):
  mod = cms.EDProducer('HGC3DClusterTMVASelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
