import FWCore.ParameterSet.Config as cms

def HcalChannelQualityGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalChannelQualityGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod