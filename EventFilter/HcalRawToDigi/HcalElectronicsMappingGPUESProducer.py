import FWCore.ParameterSet.Config as cms

def HcalElectronicsMappingGPUESProducer(**kwargs):
  mod = cms.ESProducer('HcalElectronicsMappingGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
