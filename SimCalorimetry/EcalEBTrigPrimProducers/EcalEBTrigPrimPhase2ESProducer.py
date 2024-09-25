import FWCore.ParameterSet.Config as cms

def EcalEBTrigPrimPhase2ESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalEBTrigPrimPhase2ESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
