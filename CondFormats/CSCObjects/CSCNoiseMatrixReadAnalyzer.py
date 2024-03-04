import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCNoiseMatrixReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
