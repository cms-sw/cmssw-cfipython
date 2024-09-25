import FWCore.ParameterSet.Config as cms

def EcalElectronicsMappingBuilder(*args, **kwargs):
  mod = cms.ESProducer('EcalElectronicsMappingBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
