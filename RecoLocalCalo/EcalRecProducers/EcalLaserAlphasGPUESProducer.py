import FWCore.ParameterSet.Config as cms

def EcalLaserAlphasGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalLaserAlphasGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
