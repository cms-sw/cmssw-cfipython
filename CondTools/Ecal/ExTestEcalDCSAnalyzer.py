import FWCore.ParameterSet.Config as cms

def ExTestEcalDCSAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalDCSAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
