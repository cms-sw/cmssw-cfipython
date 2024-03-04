import FWCore.ParameterSet.Config as cms

def CSCTFanalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCTFanalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
