import FWCore.ParameterSet.Config as cms

def HcalGainsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalGainsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
