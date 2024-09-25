import FWCore.ParameterSet.Config as cms

def TrackerInteractionGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrackerInteractionGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
