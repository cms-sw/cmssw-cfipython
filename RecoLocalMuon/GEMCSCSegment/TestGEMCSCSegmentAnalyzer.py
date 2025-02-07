import FWCore.ParameterSet.Config as cms

def TestGEMCSCSegmentAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGEMCSCSegmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
