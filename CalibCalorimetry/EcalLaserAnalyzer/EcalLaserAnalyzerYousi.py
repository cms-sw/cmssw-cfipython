import FWCore.ParameterSet.Config as cms

def EcalLaserAnalyzerYousi(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalLaserAnalyzerYousi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
