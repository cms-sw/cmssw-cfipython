import FWCore.ParameterSet.Config as cms

def CSCSegmentVisualise(**kwargs):
  mod = cms.EDAnalyzer('CSCSegmentVisualise',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
