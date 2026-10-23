import FWCore.ParameterSet.Config as cms

def TestConverter(*args, **kwargs):
  mod = cms.EDAnalyzer('TestConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
