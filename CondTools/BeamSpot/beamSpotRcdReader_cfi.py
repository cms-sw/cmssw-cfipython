import FWCore.ParameterSet.Config as cms

beamSpotRcdReader = cms.EDAnalyzer('BeamSpotRcdReader',
  rawFileName = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
