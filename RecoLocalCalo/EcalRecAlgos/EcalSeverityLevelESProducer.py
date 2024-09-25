import FWCore.ParameterSet.Config as cms

def EcalSeverityLevelESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalSeverityLevelESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
