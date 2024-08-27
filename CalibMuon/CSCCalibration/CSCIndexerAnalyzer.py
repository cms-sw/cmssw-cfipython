import FWCore.ParameterSet.Config as cms

def CSCIndexerAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCIndexerAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
