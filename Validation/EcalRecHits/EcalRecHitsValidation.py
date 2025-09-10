import FWCore.ParameterSet.Config as cms

def EcalRecHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
