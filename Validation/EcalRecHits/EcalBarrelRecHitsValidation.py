import FWCore.ParameterSet.Config as cms

def EcalBarrelRecHitsValidation(**kwargs):
  mod = cms.EDProducer('EcalBarrelRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
