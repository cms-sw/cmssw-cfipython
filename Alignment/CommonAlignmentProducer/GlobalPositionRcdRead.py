import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdRead(**kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
