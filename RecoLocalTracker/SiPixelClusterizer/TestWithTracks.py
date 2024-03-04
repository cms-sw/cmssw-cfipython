import FWCore.ParameterSet.Config as cms

def TestWithTracks(**kwargs):
  mod = cms.EDAnalyzer('TestWithTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
