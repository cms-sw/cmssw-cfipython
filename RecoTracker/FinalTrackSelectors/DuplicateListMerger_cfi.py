import FWCore.ParameterSet.Config as cms

DuplicateListMerger = cms.EDProducer('DuplicateListMerger',
  mergedSource = cms.InputTag(''),
  originalSource = cms.InputTag(''),
  mergedMVAVals = cms.InputTag(''),
  originalMVAVals = cms.InputTag(''),
  candidateSource = cms.InputTag(''),
  candidateComponents = cms.InputTag(''),
  diffHitsCut = cms.int32(5)
)
