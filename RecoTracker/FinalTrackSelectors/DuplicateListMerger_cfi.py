import FWCore.ParameterSet.Config as cms

DuplicateListMerger = cms.EDProducer('DuplicateListMerger',
  mergedSource = cms.InputTag(''),
  originalSource = cms.InputTag(''),
  mergedMVAVals = cms.InputTag(''),
  originalMVAVals = cms.InputTag(''),
  candidateSource = cms.InputTag(''),
  candidateComponents = cms.InputTag(''),
  trackAlgoPriorityOrder = cms.string('trackAlgoPriorityOrder'),
  diffHitsCut = cms.int32(5),
  copyExtras = cms.untracked.bool(True),
  copyTrajectories = cms.untracked.bool(False)
)
