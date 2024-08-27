import FWCore.ParameterSet.Config as cms

def TestIsoSimTracks(**kwargs):
  mod = cms.EDAnalyzer('TestIsoSimTracks',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
