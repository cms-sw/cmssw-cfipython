import FWCore.ParameterSet.Config as cms

def HcalQIECodersGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalQIECodersGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
