import FWCore.ParameterSet.Config as cms

def L1TExtCondLegacyToStage2(**kwargs):
  mod = cms.EDProducer('L1TExtCondLegacyToStage2',
    bxFirst = cms.int32(-2),
    bxLast = cms.int32(2),
    LegacyGtReadoutRecord = cms.InputTag('unpackLegacyGtDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
