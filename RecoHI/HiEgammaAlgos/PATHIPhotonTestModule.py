import FWCore.ParameterSet.Config as cms

def PATHIPhotonTestModule(**kwargs):
  mod = cms.EDAnalyzer('PATHIPhotonTestModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
