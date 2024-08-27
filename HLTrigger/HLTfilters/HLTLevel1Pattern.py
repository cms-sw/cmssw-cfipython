import FWCore.ParameterSet.Config as cms

def HLTLevel1Pattern(**kwargs):
  mod = cms.EDFilter('HLTLevel1Pattern',
    L1GtReadoutRecordTag = cms.InputTag('hltGtDigis'),
    triggerBit = cms.string('L1Tech_RPC_TTU_pointing_Cosmics.v0'),
    bunchCrossings = cms.vint32(
      -2,
      -1,
      0,
      1,
      2
    ),
    daqPartitions = cms.uint32(1),
    ignoreL1Mask = cms.bool(False),
    invert = cms.bool(False),
    throw = cms.bool(True),
    triggerPattern = cms.vint32(
      1,
      1,
      1,
      0,
      0
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
