import FWCore.ParameterSet.Config as cms

def EcalPreshowerRecHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalPreshowerRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
