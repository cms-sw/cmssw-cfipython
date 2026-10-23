import FWCore.ParameterSet.Config as cms

def CSCTFanalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCTFanalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
