import FWCore.ParameterSet.Config as cms

def CSCGACwithB(**kwargs):
  mod = cms.EDAnalyzer('CSCGACwithB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
