import FWCore.ParameterSet.Config as cms

def CSCMapperTestStartup(**kwargs):
  mod = cms.EDAnalyzer('CSCMapperTestStartup',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
