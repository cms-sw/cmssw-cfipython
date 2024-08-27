import FWCore.ParameterSet.Config as cms

def EcalRecHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
