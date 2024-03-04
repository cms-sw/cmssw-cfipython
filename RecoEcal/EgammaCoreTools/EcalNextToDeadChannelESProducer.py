import FWCore.ParameterSet.Config as cms

def EcalNextToDeadChannelESProducer(**kwargs):
  mod = cms.ESProducer('EcalNextToDeadChannelESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
