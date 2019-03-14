import FWCore.ParameterSet.Config as cms

TrackCollectionFilterCloner = cms.EDProducer('TrackCollectionFilterCloner',
  originalSource = cms.InputTag(''),
  originalMVAVals = cms.InputTag(''),
  originalQualVals = cms.InputTag(''),
  minQuality = cms.string('loose'),
  copyExtras = cms.untracked.bool(True),
  copyTrajectories = cms.untracked.bool(False)
)
