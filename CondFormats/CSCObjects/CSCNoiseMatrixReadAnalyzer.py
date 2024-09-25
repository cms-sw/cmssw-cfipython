import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
