import FWCore.ParameterSet.Config as cms

def HcalTrigPrimDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('HcalTrigPrimDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
