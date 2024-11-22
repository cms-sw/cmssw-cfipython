import FWCore.ParameterSet.Config as cms

def TestMergeResults(*args, **kwargs):
  mod = cms.EDAnalyzer('TestMergeResults',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
