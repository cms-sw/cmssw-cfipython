import FWCore.ParameterSet.Config as cms

def MuonErrorMatrixAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('MuonErrorMatrixAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
