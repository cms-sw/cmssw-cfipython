import FWCore.ParameterSet.Config as cms

def ExTestEcalIntercalibAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalIntercalibAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
