import FWCore.ParameterSet.Config as cms

def TrackerInteractionGeometryESProducer(**kwargs):
  mod = cms.ESProducer('TrackerInteractionGeometryESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
