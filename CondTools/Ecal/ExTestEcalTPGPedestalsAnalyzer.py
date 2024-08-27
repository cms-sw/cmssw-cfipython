import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPedestalsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPedestalsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
