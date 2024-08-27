import FWCore.ParameterSet.Config as cms

def Phase2TrackerClusterizer(**kwargs):
  mod = cms.EDProducer('Phase2TrackerClusterizer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
