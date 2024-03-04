import FWCore.ParameterSet.Config as cms

def CSCTFAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCTFAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
