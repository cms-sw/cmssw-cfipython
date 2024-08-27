import FWCore.ParameterSet.Config as cms

def EcalTimeCalibConstantsGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalTimeCalibConstantsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
