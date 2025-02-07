import FWCore.ParameterSet.Config as cms

def TestMuons(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMuons',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
