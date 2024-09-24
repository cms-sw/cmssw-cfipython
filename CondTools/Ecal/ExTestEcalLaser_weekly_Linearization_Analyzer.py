import FWCore.ParameterSet.Config as cms

def ExTestEcalLaser_weekly_Linearization_Analyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalLaser_weekly_Linearization_Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod