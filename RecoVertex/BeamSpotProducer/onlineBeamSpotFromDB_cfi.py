import FWCore.ParameterSet.Config as cms

onlineBeamSpotFromDB = cms.EDAnalyzer('OnlineBeamSpotFromDB',
  mightGet = cms.optional.untracked.vstring
)
