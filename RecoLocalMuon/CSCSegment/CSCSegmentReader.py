import FWCore.ParameterSet.Config as cms

def CSCSegmentReader(**kwargs):
  mod = cms.EDAnalyzer('CSCSegmentReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
