import FWCore.ParameterSet.Config as cms

def TauValMuonViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('TauValMuonViewCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
