import FWCore.ParameterSet.Config as cms

def TestGEMCSCSegmentAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestGEMCSCSegmentAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
