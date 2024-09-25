import FWCore.ParameterSet.Config as cms

def TestWithTracks(*args, **kwargs):
  mod = cms.EDAnalyzer('TestWithTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
