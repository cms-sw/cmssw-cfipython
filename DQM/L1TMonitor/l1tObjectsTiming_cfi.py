import FWCore.ParameterSet.Config as cms

l1tObjectsTiming = cms.EDProducer('L1TObjectsTiming',
  monitorDir = cms.untracked.string(''),
  verbose = cms.untracked.bool(False),
  firstBXInTrainAlgo = cms.untracked.string(''),
  lastBXInTrainAlgo = cms.untracked.string('')
)
