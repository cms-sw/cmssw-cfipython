import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadXTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadXTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
