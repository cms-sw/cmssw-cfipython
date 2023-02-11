import FWCore.ParameterSet.Config as cms

vtxTester = cms.EDAnalyzer('VtxTester',
  src = cms.InputTag('generatorSmeared'),
  mightGet = cms.optional.untracked.vstring
)
