import FWCore.ParameterSet.Config as cms

def MCMultiSignatureFilter(**kwargs):
  mod = cms.EDFilter('MCMultiSignatureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
