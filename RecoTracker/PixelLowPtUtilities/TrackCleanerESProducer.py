import FWCore.ParameterSet.Config as cms

def TrackCleanerESProducer(**kwargs):
  mod = cms.ESProducer('TrackCleanerESProducer',
    ComponentName = cms.string('trackCleaner'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
