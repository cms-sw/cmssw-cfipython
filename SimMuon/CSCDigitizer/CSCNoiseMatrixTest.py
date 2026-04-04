import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixTest(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
