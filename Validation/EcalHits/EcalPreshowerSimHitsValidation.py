import FWCore.ParameterSet.Config as cms

def EcalPreshowerSimHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalPreshowerSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
