import FWCore.ParameterSet.Config as cms

def CSCCrosstalkPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCCrosstalkPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
