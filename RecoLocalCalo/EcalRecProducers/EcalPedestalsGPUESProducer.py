import FWCore.ParameterSet.Config as cms

def EcalPedestalsGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalPedestalsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
