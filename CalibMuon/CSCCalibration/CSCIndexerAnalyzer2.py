import FWCore.ParameterSet.Config as cms

def CSCIndexerAnalyzer2(**kwargs):
  mod = cms.EDAnalyzer('CSCIndexerAnalyzer2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
