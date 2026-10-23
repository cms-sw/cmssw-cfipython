import FWCore.ParameterSet.Config as cms

def TotemVFATRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('TotemVFATRawToDigi',
    rawDataTag = cms.InputTag(''),
    subSystem = cms.string(''),
    fedIds = cms.vuint32(),
    RawUnpacking = cms.PSet(
      verbosity = cms.untracked.uint32(0)
    ),
    RawToDigi = cms.PSet(
      verbosity = cms.untracked.uint32(0),
      testFootprint = cms.uint32(2),
      testCRC = cms.uint32(2),
      testID = cms.uint32(2),
      testECMostFrequent = cms.uint32(2),
      testBCMostFrequent = cms.uint32(2),
      EC_min = cms.untracked.uint32(10),
      BC_min = cms.untracked.uint32(10),
      EC_fraction = cms.untracked.double(0.6),
      BC_fraction = cms.untracked.double(0.6),
      useOlderT2TestFile = cms.bool(False),
      printErrorSummary = cms.untracked.bool(False),
      printUnknownFrameSummary = cms.untracked.bool(False)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
