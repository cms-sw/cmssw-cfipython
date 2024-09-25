import FWCore.ParameterSet.Config as cms

def EcalPulseShapesGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalPulseShapesGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
