import FWCore.ParameterSet.Config as cms

def HcalDigisValidation(*args, **kwargs):
  mod = cms.EDProducer('HcalDigisValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
