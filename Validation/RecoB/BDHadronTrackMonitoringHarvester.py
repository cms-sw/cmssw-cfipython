import FWCore.ParameterSet.Config as cms

def BDHadronTrackMonitoringHarvester(**kwargs):
  mod = cms.EDProducer('BDHadronTrackMonitoringHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
