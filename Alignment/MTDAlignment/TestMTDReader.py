import FWCore.ParameterSet.Config as cms

def TestMTDReader(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMTDReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
