import FWCore.ParameterSet.Config as cms

def CSCIndexerAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCIndexerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
