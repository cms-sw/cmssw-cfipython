import FWCore.ParameterSet.Config as cms

def EcalGainRatiosGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalGainRatiosGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
