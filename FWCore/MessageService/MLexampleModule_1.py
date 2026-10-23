import FWCore.ParameterSet.Config as cms

def MLexampleModule_1(*args, **kwargs):
  mod = cms.EDAnalyzer('MLexampleModule_1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
