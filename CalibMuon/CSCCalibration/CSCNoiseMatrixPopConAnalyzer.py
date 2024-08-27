import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
