import FWCore.ParameterSet.Config as cms

def HcalSimHitsValidation(*args, **kwargs):
  mod = cms.EDProducer('HcalSimHitsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
