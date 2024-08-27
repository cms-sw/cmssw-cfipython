import FWCore.ParameterSet.Config as cms

def CSCOfflineMonitor(**kwargs):
  mod = cms.EDProducer('CSCOfflineMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
