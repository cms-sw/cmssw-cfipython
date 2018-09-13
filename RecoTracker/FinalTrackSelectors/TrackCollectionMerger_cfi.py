import FWCore.ParameterSet.Config as cms

TrackCollectionMerger = cms.EDProducer('TrackCollectionMerger',
  trackProducers = cms.VInputTag(),
  inputClassifiers = cms.vstring(),
  shareFrac = cms.double(0.19),
  foundHitBonus = cms.double(10),
  lostHitPenalty = cms.double(5),
  minShareHits = cms.uint32(2),
  allowFirstHitShare = cms.bool(True),
  minQuality = cms.string('loose')
)
