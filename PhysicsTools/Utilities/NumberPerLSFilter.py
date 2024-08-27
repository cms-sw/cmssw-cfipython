import FWCore.ParameterSet.Config as cms

def NumberPerLSFilter(**kwargs):
  mod = cms.EDFilter('NumberPerLSFilter',
    maxN = cms.int32(100),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
