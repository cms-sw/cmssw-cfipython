import FWCore.ParameterSet.Config as cms

def OOTPileupDBCompatibilityESProducer(*args, **kwargs):
  mod = cms.ESProducer('OOTPileupDBCompatibilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
