import FWCore.ParameterSet.Config as cms

def TrackCleanerESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrackCleanerESProducer',
    ComponentName = cms.string('trackCleaner'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
