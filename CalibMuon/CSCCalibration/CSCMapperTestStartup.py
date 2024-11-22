import FWCore.ParameterSet.Config as cms

def CSCMapperTestStartup(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCMapperTestStartup',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
