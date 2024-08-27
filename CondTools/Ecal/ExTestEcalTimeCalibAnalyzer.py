import FWCore.ParameterSet.Config as cms

def ExTestEcalTimeCalibAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTimeCalibAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
