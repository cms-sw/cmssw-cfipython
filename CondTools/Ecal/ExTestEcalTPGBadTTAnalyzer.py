import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadTTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadTTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
