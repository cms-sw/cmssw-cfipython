import FWCore.ParameterSet.Config as cms

def CSCSegmentVisualise(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCSegmentVisualise',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
