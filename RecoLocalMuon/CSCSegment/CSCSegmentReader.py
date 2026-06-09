import FWCore.ParameterSet.Config as cms

def CSCSegmentReader(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCSegmentReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
