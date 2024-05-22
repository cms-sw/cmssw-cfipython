import FWCore.ParameterSet.Config as cms

def TrackerAdditionalParametersPerDetESModule(**kwargs):
  mod = cms.ESProducer('TrackerAdditionalParametersPerDetESModule',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
