import FWCore.ParameterSet.Config as cms

def TrackerGeometricDetESModule(*args, **kwargs):
  mod = cms.ESProducer('TrackerGeometricDetESModule',
    fromDDD = cms.bool(False),
    fromDD4hep = cms.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
