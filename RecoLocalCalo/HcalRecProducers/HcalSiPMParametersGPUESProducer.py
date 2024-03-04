import FWCore.ParameterSet.Config as cms

def HcalSiPMParametersGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalSiPMParametersGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
