import FWCore.ParameterSet.Config as cms

def CSCFakeNoiseMatrixPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCFakeNoiseMatrixPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
