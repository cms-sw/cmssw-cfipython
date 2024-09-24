import FWCore.ParameterSet.Config as cms

def L1TExtCondLegacyToStage2(*args, **kwargs):
  mod = cms.EDProducer('L1TExtCondLegacyToStage2',
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    LegacyGtReadoutRecord = cms.InputTag('unpackLegacyGtDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
