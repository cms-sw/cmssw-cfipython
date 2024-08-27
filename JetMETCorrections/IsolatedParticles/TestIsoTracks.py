import FWCore.ParameterSet.Config as cms

def TestIsoTracks(**kwargs):
  mod = cms.EDAnalyzer('TestIsoTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
