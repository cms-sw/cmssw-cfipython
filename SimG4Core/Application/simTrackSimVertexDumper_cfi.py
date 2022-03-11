import FWCore.ParameterSet.Config as cms

simTrackSimVertexDumper = cms.EDAnalyzer('SimTrackSimVertexDumper',
  moduleLabelHepMC = cms.InputTag('generatorSmeared'),
  moduleLabelTk = cms.InputTag('g4SimHits'),
  moduleLabelVtx = cms.InputTag('g4SimHits'),
  dumpHepMC = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
