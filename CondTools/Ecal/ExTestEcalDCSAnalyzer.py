import FWCore.ParameterSet.Config as cms

def ExTestEcalDCSAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalDCSAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
