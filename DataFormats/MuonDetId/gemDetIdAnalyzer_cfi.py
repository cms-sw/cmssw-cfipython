import FWCore.ParameterSet.Config as cms

gemDetIdAnalyzer = cms.EDAnalyzer('GEMDetIdAnalyzer',
  gemInputLabel = cms.InputTag('gemRecHits'),
  me0InputLabel = cms.InputTag('me0RecHits'),
  newGEMDetID = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
