import FWCore.ParameterSet.Config as cms

def TrackerParametersESModule(*args, **kwargs):
  mod = cms.ESProducer('TrackerParametersESModule',
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
