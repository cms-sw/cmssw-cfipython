import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPhysicsConstAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPhysicsConstAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
