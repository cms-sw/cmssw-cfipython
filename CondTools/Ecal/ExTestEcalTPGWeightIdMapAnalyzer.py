import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGWeightIdMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGWeightIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
