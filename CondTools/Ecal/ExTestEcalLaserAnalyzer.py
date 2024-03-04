import FWCore.ParameterSet.Config as cms

def ExTestEcalLaserAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalLaserAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
