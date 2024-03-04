import FWCore.ParameterSet.Config as cms

def CSCTFConfigTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCTFConfigTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
