import FWCore.ParameterSet.Config as cms

def CSCMapperTestPostls1(*args, **kwargs):
  mod = cms.EDAnalyzer('CSCMapperTestPostls1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
