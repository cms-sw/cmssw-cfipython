import FWCore.ParameterSet.Config as cms

def TestTFileServiceAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestTFileServiceAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
