import FWCore.ParameterSet.Config as cms

def HcalSiPMCharacteristicsGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalSiPMCharacteristicsGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
