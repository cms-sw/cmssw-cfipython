import FWCore.ParameterSet.Config as cms

def EcalBarrelSimHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalBarrelSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
