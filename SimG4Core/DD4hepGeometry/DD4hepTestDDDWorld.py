import FWCore.ParameterSet.Config as cms

def DD4hepTestDDDWorld(*args, **kwargs):
  mod = cms.EDAnalyzer('DD4hepTestDDDWorld',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
