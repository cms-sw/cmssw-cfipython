import FWCore.ParameterSet.Config as cms

def TransientTrackBuilderESProducer(*args, **kwargs):
  mod = cms.ESProducer('TransientTrackBuilderESProducer',
    ComponentName = cms.string('TransientTrackBuilder'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
