import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGWeightGroupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGWeightGroupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
