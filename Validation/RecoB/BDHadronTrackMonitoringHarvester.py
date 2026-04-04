import FWCore.ParameterSet.Config as cms

def BDHadronTrackMonitoringHarvester(*args, **kwargs):
  mod = cms.EDProducer('BDHadronTrackMonitoringHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
