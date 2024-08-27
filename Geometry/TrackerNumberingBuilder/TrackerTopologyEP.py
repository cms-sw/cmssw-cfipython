import FWCore.ParameterSet.Config as cms

def TrackerTopologyEP(**kwargs):
  mod = cms.ESProducer('TrackerTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
