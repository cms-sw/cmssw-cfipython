import FWCore.ParameterSet.Config as cms

def RecoCandViewRefSelector(**kwargs):
  mod = cms.EDFilter('RecoCandViewRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
