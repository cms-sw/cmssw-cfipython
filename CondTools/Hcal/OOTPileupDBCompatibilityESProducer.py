import FWCore.ParameterSet.Config as cms

def OOTPileupDBCompatibilityESProducer(**kwargs):
  mod = cms.ESProducer('OOTPileupDBCompatibilityESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
