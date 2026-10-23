import FWCore.ParameterSet.Config as cms

def PATCandViewCountFilter(*args, **kwargs):
  mod = cms.EDFilter('PATCandViewCountFilter',
    src = cms.InputTag(''),
    minNumber = cms.uint32(0),
    maxNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
