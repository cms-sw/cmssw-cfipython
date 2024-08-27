import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadXTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadXTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
