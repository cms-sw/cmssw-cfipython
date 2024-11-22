import FWCore.ParameterSet.Config as cms

def ExTestEcalSRPAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalSRPAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
