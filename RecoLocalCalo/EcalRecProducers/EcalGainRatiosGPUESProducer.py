import FWCore.ParameterSet.Config as cms

def EcalGainRatiosGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalGainRatiosGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
