import FWCore.ParameterSet.Config as cms

def CSCTFConfigTestAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCTFConfigTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
