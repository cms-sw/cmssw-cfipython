import FWCore.ParameterSet.Config as cms

def RPCAMCRawToDigi(*args, **kwargs):
  mod = cms.EDProducer('RPCAMCRawToDigi',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
