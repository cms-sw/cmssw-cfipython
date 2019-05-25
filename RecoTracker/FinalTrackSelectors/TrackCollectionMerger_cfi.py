import FWCore.ParameterSet.Config as cms

TrackCollectionMerger = cms.EDProducer('TrackCollectionMerger',
  trackProducers = cms.VInputTag(),
  inputClassifiers = cms.vstring(),
  trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
  shareFrac = cms.double(0.19),
  foundHitBonus = cms.double(10),
  lostHitPenalty = cms.double(5),
  minShareHits = cms.uint32(2),
  allowFirstHitShare = cms.bool(True),
  enableMerging = cms.bool(True),
  minQuality = cms.string('loose'),
  copyExtras = cms.untracked.bool(True),
  copyTrajectories = cms.untracked.bool(False)
)
