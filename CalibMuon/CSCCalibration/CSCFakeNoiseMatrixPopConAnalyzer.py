import FWCore.ParameterSet.Config as cms

def CSCFakeNoiseMatrixPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCFakeNoiseMatrixPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
