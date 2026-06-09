import FWCore.ParameterSet.Config as cms

def L1TMP7ZeroSupp(*args, **kwargs):
  mod = cms.EDProducer('L1TMP7ZeroSupp',
    rawData = cms.required.InputTag,
    fedIds = cms.required.vint32,
    zsEnabled = cms.untracked.bool(True),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8),
    lenAMC13Header = cms.untracked.int32(8),
    lenAMC13Trailer = cms.untracked.int32(8),
    lenAMCHeader = cms.untracked.int32(8),
    lenAMCTrailer = cms.untracked.int32(0),
    zsFlagMask = cms.untracked.int32(1),
    newZsFlagMask = cms.untracked.int32(2),
    dataInvFlagMask = cms.untracked.int32(1),
    maxFEDReadoutSize = cms.untracked.int32(10000),
    maskCapId0 = cms.optional.untracked.vint32,
    maskCapId1 = cms.optional.untracked.vint32,
    maskCapId2 = cms.optional.untracked.vint32,
    maskCapId3 = cms.optional.untracked.vint32,
    maskCapId4 = cms.optional.untracked.vint32,
    maskCapId5 = cms.optional.untracked.vint32,
    maskCapId6 = cms.optional.untracked.vint32,
    maskCapId7 = cms.optional.untracked.vint32,
    maskCapId8 = cms.optional.untracked.vint32,
    maskCapId9 = cms.optional.untracked.vint32,
    maskCapId10 = cms.optional.untracked.vint32,
    maskCapId11 = cms.optional.untracked.vint32,
    maskCapId12 = cms.optional.untracked.vint32,
    maskCapId13 = cms.optional.untracked.vint32,
    maskCapId14 = cms.optional.untracked.vint32,
    maskCapId15 = cms.optional.untracked.vint32,
    checkOnlyCapIdsWithMasks = cms.untracked.bool(True),
    monitorDir = cms.untracked.string(''),
    verbose = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
