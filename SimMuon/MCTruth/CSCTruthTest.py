import FWCore.ParameterSet.Config as cms

def CSCTruthTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCTruthTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
