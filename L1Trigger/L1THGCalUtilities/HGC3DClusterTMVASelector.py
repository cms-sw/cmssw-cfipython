import FWCore.ParameterSet.Config as cms

def HGC3DClusterTMVASelector(**kwargs):
  mod = cms.EDProducer('HGC3DClusterTMVASelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
