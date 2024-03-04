import FWCore.ParameterSet.Config as cms

def TauValMuonViewCleaner(**kwargs):
  mod = cms.EDProducer('TauValMuonViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
