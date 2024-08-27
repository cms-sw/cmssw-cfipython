import FWCore.ParameterSet.Config as cms

def ExTestEcalADCToGeVAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalADCToGeVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
