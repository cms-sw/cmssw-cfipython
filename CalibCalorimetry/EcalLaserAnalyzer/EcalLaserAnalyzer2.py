import FWCore.ParameterSet.Config as cms

def EcalLaserAnalyzer2(**kwargs):
  mod = cms.EDAnalyzer('EcalLaserAnalyzer2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod