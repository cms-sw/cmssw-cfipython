import FWCore.ParameterSet.Config as cms

def EcalElectronicsMappingBuilder(**kwargs):
  mod = cms.ESProducer('EcalElectronicsMappingBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
