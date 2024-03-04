import FWCore.ParameterSet.Config as cms

def HcalTB02ParametersESModule(**kwargs):
  mod = cms.ESProducer('HcalTB02ParametersESModule',
    name = cms.string('EcalHitsEB'),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
