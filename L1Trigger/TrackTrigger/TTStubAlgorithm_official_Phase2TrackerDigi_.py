import FWCore.ParameterSet.Config as cms

def TTStubAlgorithm_official_Phase2TrackerDigi_(*args, **kwargs):
  mod = cms.ESProducer('TTStubAlgorithm_official_Phase2TrackerDigi_',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
