import FWCore.ParameterSet.Config as cms

def TTStubAlgorithm_official_Phase2TrackerDigi_(**kwargs):
  mod = cms.ESProducer('TTStubAlgorithm_official_Phase2TrackerDigi_',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
