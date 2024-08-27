import FWCore.ParameterSet.Config as cms

def HGC3DClusterGenMatchSelector(**kwargs):
  mod = cms.EDProducer('HGC3DClusterGenMatchSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
