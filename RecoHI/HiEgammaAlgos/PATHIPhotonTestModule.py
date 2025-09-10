import FWCore.ParameterSet.Config as cms

def PATHIPhotonTestModule(*args, **kwargs):
  mod = cms.EDAnalyzer('PATHIPhotonTestModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
