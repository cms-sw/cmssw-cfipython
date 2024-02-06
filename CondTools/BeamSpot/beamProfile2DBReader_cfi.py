import FWCore.ParameterSet.Config as cms

beamProfile2DBReader = cms.EDAnalyzer('BeamProfile2DBReader',
  rawFileName = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
