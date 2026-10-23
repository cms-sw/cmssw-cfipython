import FWCore.ParameterSet.Config as cms

def EcalBarrelSimHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalBarrelSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
