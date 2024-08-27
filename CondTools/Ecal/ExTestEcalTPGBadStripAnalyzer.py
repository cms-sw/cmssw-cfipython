import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadStripAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadStripAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
