import FWCore.ParameterSet.Config as cms

def TestIsoSimTracks(*args, **kwargs):
  mod = cms.EDAnalyzer('TestIsoSimTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
