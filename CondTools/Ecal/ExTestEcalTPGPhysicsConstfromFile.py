import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPhysicsConstfromFile(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPhysicsConstfromFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
