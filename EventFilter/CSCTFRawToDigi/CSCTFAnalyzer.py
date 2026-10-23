import FWCore.ParameterSet.Config as cms

def CSCTFAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCTFAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
