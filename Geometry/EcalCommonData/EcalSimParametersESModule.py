import FWCore.ParameterSet.Config as cms

def EcalSimParametersESModule(**kwargs):
  mod = cms.ESProducer('EcalSimParametersESModule',
    fromDD4hep = cms.bool(False),
    name = cms.string('EcalHitsEB'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
