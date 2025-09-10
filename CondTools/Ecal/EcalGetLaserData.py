import FWCore.ParameterSet.Config as cms

def EcalGetLaserData(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalGetLaserData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
