import FWCore.ParameterSet.Config as cms

Primary4DVertexPostProcessor = cms.EDProducer('Primary4DVertexHarvester',
  folder = cms.string('MTD/Vertices/'),
  mightGet = cms.optional.untracked.vstring
)
