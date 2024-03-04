import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdWrite(**kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
