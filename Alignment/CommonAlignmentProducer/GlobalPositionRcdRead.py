import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdRead(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
