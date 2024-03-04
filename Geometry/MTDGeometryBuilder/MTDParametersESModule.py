import FWCore.ParameterSet.Config as cms

def MTDParametersESModule(**kwargs):
  mod = cms.ESProducer('MTDParametersESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
