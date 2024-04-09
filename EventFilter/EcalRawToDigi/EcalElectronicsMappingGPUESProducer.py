import FWCore.ParameterSet.Config as cms

def EcalElectronicsMappingGPUESProducer(**kwargs):
  mod = cms.ESProducer('EcalElectronicsMappingGPUESProducer',
    ComponentName = cms.string(''),
    label = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod