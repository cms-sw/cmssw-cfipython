import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGBadTTAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGBadTTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
