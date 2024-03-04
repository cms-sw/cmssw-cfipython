import FWCore.ParameterSet.Config as cms

def CSCOfflineClient(**kwargs):
  mod = cms.EDProducer('CSCOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
