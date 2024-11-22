import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGOddWeightIdMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGOddWeightIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
