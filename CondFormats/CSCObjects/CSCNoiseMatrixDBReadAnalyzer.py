import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixDBReadAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
