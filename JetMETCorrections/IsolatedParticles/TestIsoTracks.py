import FWCore.ParameterSet.Config as cms

def TestIsoTracks(*args, **kwargs):
  mod = cms.EDAnalyzer('TestIsoTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
