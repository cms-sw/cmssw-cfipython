import FWCore.ParameterSet.Config as cms

hgcalDigis = cms.EDProducer('HGCalRawToDigi',
  src = cms.InputTag('rawDataCollector'),
  maxCaptureBlock = cms.uint32(1),
  captureBlockReserved = cms.uint32(0),
  econdHeaderMarker = cms.uint32(340),
  slinkBOE = cms.uint32(42),
  captureBlockECONDMax = cms.uint32(12),
  econdERXMax = cms.uint32(12),
  erxChannelMax = cms.uint32(37),
  payloadLengthMax = cms.uint32(469),
  channelMax = cms.uint32(7000000),
  commonModeMax = cms.uint32(4000000),
  badECONDMax = cms.uint32(200),
  fedIds = cms.vuint32(),
  numERxsInECOND = cms.uint32(12),
  mightGet = cms.optional.untracked.vstring
)
