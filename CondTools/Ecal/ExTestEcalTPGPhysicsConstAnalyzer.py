import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPhysicsConstAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPhysicsConstAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
