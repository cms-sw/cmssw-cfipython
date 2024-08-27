import FWCore.ParameterSet.Config as cms

def HcalHitReconstructor(**kwargs):
  mod = cms.EDProducer('HcalHitReconstructor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
