import FWCore.ParameterSet.Config as cms

def EcalPreshowerSimHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalPreshowerSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
