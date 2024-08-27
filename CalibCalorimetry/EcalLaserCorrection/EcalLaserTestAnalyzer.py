import FWCore.ParameterSet.Config as cms

def EcalLaserTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalLaserTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
