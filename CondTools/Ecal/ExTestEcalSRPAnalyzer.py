import FWCore.ParameterSet.Config as cms

def ExTestEcalSRPAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalSRPAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
