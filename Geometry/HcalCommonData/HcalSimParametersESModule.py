import FWCore.ParameterSet.Config as cms

def HcalSimParametersESModule(**kwargs):
  mod = cms.ESProducer('HcalSimParametersESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
