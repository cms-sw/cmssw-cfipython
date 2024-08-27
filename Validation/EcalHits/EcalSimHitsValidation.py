import FWCore.ParameterSet.Config as cms

def EcalSimHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
