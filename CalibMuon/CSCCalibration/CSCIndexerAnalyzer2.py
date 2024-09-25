import FWCore.ParameterSet.Config as cms

def CSCIndexerAnalyzer2(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCIndexerAnalyzer2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
