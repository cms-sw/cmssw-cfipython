import FWCore.ParameterSet.Config as cms

def HGC3DClusterSimpleSelector(*args, **kwargs):
  mod = cms.EDProducer('HGC3DClusterSimpleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
