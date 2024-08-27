import FWCore.ParameterSet.Config as cms

def HGCalSlinkEmulator(**kwargs):
  mod = cms.EDProducer('HGCalSlinkEmulator',
    slinkParams = cms.PSet(
      ECONDs = cms.VPSet(
        cms.PSet(),
        cms.PSet(),
        cms.PSet(),
        cms.PSet(),
        cms.PSet(),
        cms.PSet(),
        cms.PSet()
      ),
      boeMarker = cms.uint32(85),
      eoeMarker = cms.uint32(170),
      formatVersion = cms.uint32(3),
      numCaptureBlocks = cms.uint32(1),
      checkECONDsLimits = cms.bool(True),
      storeHeaderTrailer = cms.bool(True)
    ),
    emulatorType = cms.string('trivial'),
    fedId = cms.uint32(0),
    fedHeaderTrailer = cms.bool(False),
    storeEmulatorInfo = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
