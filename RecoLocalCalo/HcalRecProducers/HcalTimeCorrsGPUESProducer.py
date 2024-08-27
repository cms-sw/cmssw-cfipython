import FWCore.ParameterSet.Config as cms

def HcalTimeCorrsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalTimeCorrsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
