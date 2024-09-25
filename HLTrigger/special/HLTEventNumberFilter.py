import FWCore.ParameterSet.Config as cms

def HLTEventNumberFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTEventNumberFilter',
    period = cms.int32(4096),
    invert = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
