import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLinPed_Analyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLinPed_Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
