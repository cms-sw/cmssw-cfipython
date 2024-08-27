import FWCore.ParameterSet.Config as cms

def ZdcHitReconstructor(**kwargs):
  mod = cms.EDProducer('ZdcHitReconstructor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
