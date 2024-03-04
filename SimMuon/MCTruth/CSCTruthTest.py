import FWCore.ParameterSet.Config as cms

def CSCTruthTest(**kwargs):
  mod = cms.EDAnalyzer('CSCTruthTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
