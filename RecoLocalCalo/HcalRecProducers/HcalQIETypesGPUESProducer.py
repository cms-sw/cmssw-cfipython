import FWCore.ParameterSet.Config as cms

def HcalQIETypesGPUESProducer(*args, **kwargs):
  mod = cms.ESProducer('HcalQIETypesGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
