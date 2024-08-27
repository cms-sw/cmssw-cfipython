import FWCore.ParameterSet.Config as cms

def HcalQIETypesGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalQIETypesGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
