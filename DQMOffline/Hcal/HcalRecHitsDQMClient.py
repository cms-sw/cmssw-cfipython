import FWCore.ParameterSet.Config as cms

def HcalRecHitsDQMClient(**kwargs):
  mod = cms.EDProducer('HcalRecHitsDQMClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
