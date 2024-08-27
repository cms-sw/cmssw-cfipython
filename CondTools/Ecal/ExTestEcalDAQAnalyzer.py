import FWCore.ParameterSet.Config as cms

def ExTestEcalDAQAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalDAQAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
