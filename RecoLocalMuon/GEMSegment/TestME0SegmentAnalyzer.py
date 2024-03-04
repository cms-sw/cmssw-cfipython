import FWCore.ParameterSet.Config as cms

def TestME0SegmentAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestME0SegmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
