import FWCore.ParameterSet.Config as cms

def HcalRecHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('HcalRecHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
