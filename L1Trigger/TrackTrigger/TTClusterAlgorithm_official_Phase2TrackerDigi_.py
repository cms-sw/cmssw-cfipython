import FWCore.ParameterSet.Config as cms

def TTClusterAlgorithm_official_Phase2TrackerDigi_(*args, **kwargs):
  mod = cms.ESProducer('TTClusterAlgorithm_official_Phase2TrackerDigi_',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
