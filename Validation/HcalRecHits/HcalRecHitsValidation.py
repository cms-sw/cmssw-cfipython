import FWCore.ParameterSet.Config as cms

def HcalRecHitsValidation(**kwargs):
  mod = cms.EDProducer('HcalRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
