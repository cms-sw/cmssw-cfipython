import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLinConstAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLinConstAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
