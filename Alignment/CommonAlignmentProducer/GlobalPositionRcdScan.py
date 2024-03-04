import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdScan(**kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdScan',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
