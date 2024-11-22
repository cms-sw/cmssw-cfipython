import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGPedestalsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGPedestalsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
