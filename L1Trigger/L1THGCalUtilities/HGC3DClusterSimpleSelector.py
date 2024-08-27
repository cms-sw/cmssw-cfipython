import FWCore.ParameterSet.Config as cms

def HGC3DClusterSimpleSelector(**kwargs):
  mod = cms.EDProducer('HGC3DClusterSimpleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
