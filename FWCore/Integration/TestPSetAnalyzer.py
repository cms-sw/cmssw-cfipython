import FWCore.ParameterSet.Config as cms

def TestPSetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestPSetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
