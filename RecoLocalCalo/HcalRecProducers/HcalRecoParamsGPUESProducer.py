import FWCore.ParameterSet.Config as cms

def HcalRecoParamsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalRecoParamsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
