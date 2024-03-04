import FWCore.ParameterSet.Config as cms

def Phase2TrackerMonitorDigi(**kwargs):
  mod = cms.EDProducer('Phase2TrackerMonitorDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
