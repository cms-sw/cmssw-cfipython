import FWCore.ParameterSet.Config as cms

def ExTestEcalPedestalsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalPedestalsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
