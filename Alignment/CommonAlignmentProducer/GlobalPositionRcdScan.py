import FWCore.ParameterSet.Config as cms

def GlobalPositionRcdScan(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalPositionRcdScan',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
