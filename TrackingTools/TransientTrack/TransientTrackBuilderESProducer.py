import FWCore.ParameterSet.Config as cms

def TransientTrackBuilderESProducer(**kwargs):
  mod = cms.ESProducer('TransientTrackBuilderESProducer',
    ComponentName = cms.string('TransientTrackBuilder'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod