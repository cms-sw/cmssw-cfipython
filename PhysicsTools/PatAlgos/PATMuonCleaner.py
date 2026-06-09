import FWCore.ParameterSet.Config as cms

def PATMuonCleaner(*args, **kwargs):
  mod = cms.EDProducer('PATMuonCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
