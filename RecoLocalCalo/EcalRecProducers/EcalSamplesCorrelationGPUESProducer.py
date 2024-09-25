import FWCore.ParameterSet.Config as cms

def EcalSamplesCorrelationGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalSamplesCorrelationGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
