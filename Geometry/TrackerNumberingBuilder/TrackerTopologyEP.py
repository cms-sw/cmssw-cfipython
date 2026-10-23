import FWCore.ParameterSet.Config as cms

def TrackerTopologyEP(*args, **kwargs):
  mod = cms.ESProducer('TrackerTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
