import FWCore.ParameterSet.Config as cms

hltPPSPerPotTrackFilter = cms.EDFilter('HLTPPSPerPotTrackFilter',
  pixelLocalTrackInputTag = cms.InputTag('ctppsPixelLocalTracks'),
  stripLocalTrackInputTag = cms.InputTag('totemRPLocalTrackFitter'),
  diamondLocalTrackInputTag = cms.InputTag('ctppsDiamondLocalTracks'),
  pixelFilter = cms.VPSet(
    cms.PSet(
      detid = cms.uint32(2022703104),
      maxTracks = cms.int32(-1),
      minTracks = cms.int32(2)
    ),
    cms.PSet(
      detid = cms.uint32(2023227392),
      maxTracks = cms.int32(-1),
      minTracks = cms.int32(2)
    ),
    cms.PSet(
      detid = cms.uint32(2039480320),
      maxTracks = cms.int32(-1),
      minTracks = cms.int32(2)
    ),
    cms.PSet(
      detid = cms.uint32(2040004608),
      maxTracks = cms.int32(-1),
      minTracks = cms.int32(2)
    )
  ),
  stripFilter = cms.VPSet(
  ),
  diamondFilter = cms.VPSet(
  ),
  triggerType = cms.int32(91),
  mightGet = cms.optional.untracked.vstring
)
