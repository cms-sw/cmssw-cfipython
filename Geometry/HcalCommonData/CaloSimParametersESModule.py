import FWCore.ParameterSet.Config as cms

def CaloSimParametersESModule(**kwargs):
  mod = cms.ESProducer('CaloSimParametersESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
