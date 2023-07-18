import FWCore.ParameterSet.Config as cms

RPCAMCRawToDigi = cms.EDProducer('RPCAMCRawToDigi',
  inputTag = cms.InputTag('rawDataCollector'),
  calculateCRC = cms.bool(True),
  fillCounters = cms.bool(True),
  RPCAMCUnpacker = cms.string('RPCAMCUnpacker'),
  RPCAMCUnpackerSettings = cms.PSet(
    fillAMCCounters = cms.bool(True),
    bxMin = cms.int32(-2),
    bxMax = cms.int32(2),
    cppfDaqDelay = cms.int32(0)
  ),
  mightGet = cms.optional.untracked.vstring
)
