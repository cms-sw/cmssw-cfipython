import FWCore.ParameterSet.Config as cms

def EcalNextToDeadChannelESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalNextToDeadChannelESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod