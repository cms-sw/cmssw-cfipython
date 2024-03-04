import FWCore.ParameterSet.Config as cms

def CSCFakeGainsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCFakeGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
