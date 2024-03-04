import FWCore.ParameterSet.Config as cms

def HLTEventNumberFilter(**kwargs):
  mod = cms.EDFilter('HLTEventNumberFilter',
    period = cms.int32(4096),
    invert = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
