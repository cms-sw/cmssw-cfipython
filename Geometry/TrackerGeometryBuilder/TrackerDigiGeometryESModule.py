import FWCore.ParameterSet.Config as cms

def TrackerDigiGeometryESModule(*args, **kwargs):
  mod = cms.ESProducer('TrackerDigiGeometryESModule',
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False),
    applyAlignment = cms.bool(True),
    alignmentsLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
