import FWCore.ParameterSet.Config as cms

def StatusCandViewSelector(**kwargs):
  mod = cms.EDFilter('StatusCandViewSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
