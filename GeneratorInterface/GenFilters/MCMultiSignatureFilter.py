import FWCore.ParameterSet.Config as cms

def MCMultiSignatureFilter(*args, **kwargs):
  mod = cms.EDFilter('MCMultiSignatureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
