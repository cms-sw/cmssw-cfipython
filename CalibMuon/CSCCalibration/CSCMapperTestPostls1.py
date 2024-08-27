import FWCore.ParameterSet.Config as cms

def CSCMapperTestPostls1(**kwargs):
  mod = cms.EDAnalyzer('CSCMapperTestPostls1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
