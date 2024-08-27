import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGLinPed_Analyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGLinPed_Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
