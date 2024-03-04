import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixDBReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
