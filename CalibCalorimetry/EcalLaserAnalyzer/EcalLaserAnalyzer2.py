import FWCore.ParameterSet.Config as cms

def EcalLaserAnalyzer2(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalLaserAnalyzer2',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
