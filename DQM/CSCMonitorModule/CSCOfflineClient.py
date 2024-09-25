import FWCore.ParameterSet.Config as cms

def CSCOfflineClient(*args, **kwargs):
  mod = cms.EDProducer('CSCOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
