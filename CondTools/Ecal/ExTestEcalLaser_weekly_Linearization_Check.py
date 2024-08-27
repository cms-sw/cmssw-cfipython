import FWCore.ParameterSet.Config as cms

def ExTestEcalLaser_weekly_Linearization_Check(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalLaser_weekly_Linearization_Check',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
