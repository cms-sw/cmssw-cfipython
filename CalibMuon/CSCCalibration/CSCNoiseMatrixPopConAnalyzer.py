import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
