import FWCore.ParameterSet.Config as cms

def HcalLUTCorrsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalLUTCorrsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
