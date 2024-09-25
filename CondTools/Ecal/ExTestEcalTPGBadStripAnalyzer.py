import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadStripAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadStripAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
