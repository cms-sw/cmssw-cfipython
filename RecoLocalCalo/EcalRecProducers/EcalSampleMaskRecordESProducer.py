import FWCore.ParameterSet.Config as cms

def EcalSampleMaskRecordESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalSampleMaskRecordESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
