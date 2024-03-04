import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLinConstAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLinConstAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
