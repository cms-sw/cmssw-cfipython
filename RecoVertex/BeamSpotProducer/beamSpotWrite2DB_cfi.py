import FWCore.ParameterSet.Config as cms

beamSpotWrite2DB = cms.EDAnalyzer('BeamSpotWrite2DB',
  OutputFileName = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
