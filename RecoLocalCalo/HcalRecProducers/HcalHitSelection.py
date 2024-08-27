import FWCore.ParameterSet.Config as cms

def HcalHitSelection(**kwargs):
  mod = cms.EDProducer('HcalHitSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
