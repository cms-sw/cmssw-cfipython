import FWCore.ParameterSet.Config as cms

def EcalLaserCondTools(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalLaserCondTools',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
