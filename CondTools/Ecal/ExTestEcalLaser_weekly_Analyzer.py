import FWCore.ParameterSet.Config as cms

def ExTestEcalLaser_weekly_Analyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalLaser_weekly_Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
