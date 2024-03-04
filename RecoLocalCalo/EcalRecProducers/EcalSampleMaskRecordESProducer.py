import FWCore.ParameterSet.Config as cms

def EcalSampleMaskRecordESProducer(**kwargs):
  mod = cms.ESProducer('EcalSampleMaskRecordESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
