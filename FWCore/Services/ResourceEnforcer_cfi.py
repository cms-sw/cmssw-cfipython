import FWCore.ParameterSet.Config as cms

ResourceEnforcer = cms.Service('ResourceEnforcer',
  maxVSize = cms.untracked.double(0),
  maxRSS = cms.untracked.double(0),
  maxTime = cms.untracked.double(0)
)
