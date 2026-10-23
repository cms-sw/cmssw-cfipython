import FWCore.ParameterSet.Config as cms

def ExTestEcalADCToGeVAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalADCToGeVAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
