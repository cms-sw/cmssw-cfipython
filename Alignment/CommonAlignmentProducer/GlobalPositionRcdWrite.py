import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
