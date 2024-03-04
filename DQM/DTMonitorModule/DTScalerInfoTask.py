import FWCore.ParameterSet.Config as cms

def DTScalerInfoTask(**kwargs):
  mod = cms.EDProducer('DTScalerInfoTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
