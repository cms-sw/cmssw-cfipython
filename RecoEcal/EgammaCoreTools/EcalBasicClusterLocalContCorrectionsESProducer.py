import FWCore.ParameterSet.Config as cms

def EcalBasicClusterLocalContCorrectionsESProducer(*args, **kwargs):
  mod = cms.ESProducer('EcalBasicClusterLocalContCorrectionsESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
