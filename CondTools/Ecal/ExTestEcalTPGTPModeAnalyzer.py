import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGTPModeAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGTPModeAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
