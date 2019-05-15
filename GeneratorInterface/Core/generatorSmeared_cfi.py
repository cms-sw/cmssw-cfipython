import FWCore.ParameterSet.Config as cms

generatorSmeared = cms.EDProducer('GeneratorSmearedProducer',
  currentTag = cms.untracked.InputTag('VtxSmeared'),
  previousTag = cms.untracked.InputTag('generator')
)
