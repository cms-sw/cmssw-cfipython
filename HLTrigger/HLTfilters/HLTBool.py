import FWCore.ParameterSet.Config as cms

def HLTBool(**kwargs):
  mod = cms.EDFilter('HLTBool',
    result = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
