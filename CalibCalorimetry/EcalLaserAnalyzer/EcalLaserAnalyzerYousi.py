import FWCore.ParameterSet.Config as cms

def EcalLaserAnalyzerYousi(**kwargs):
  mod = cms.EDAnalyzer('EcalLaserAnalyzerYousi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
