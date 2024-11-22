import FWCore.ParameterSet.Config as cms

def EcalSimHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
