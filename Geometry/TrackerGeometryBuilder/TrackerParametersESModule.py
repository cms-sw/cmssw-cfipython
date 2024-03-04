import FWCore.ParameterSet.Config as cms

def TrackerParametersESModule(**kwargs):
  mod = cms.ESProducer('TrackerParametersESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
