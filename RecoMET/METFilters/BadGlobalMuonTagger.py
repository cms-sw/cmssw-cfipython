import FWCore.ParameterSet.Config as cms

def BadGlobalMuonTagger(*args, **kwargs):
  mod = cms.EDFilter('BadGlobalMuonTagger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
