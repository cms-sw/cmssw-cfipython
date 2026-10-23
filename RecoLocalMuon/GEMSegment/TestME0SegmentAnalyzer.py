import FWCore.ParameterSet.Config as cms

def TestME0SegmentAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestME0SegmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
