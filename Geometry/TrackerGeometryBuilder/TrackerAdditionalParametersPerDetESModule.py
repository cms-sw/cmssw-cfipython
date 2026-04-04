import FWCore.ParameterSet.Config as cms

def TrackerAdditionalParametersPerDetESModule(*args, **kwargs):
  mod = cms.ESProducer('TrackerAdditionalParametersPerDetESModule',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
