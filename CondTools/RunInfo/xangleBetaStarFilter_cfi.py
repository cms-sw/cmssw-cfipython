import FWCore.ParameterSet.Config as cms

xangleBetaStarFilter = cms.EDFilter('XangleBetaStarFilter',
  lhcInfoLabel = cms.string(''),
  xangle_min = cms.double(0),
  xangle_max = cms.double(1000),
  beta_star_min = cms.double(0),
  beta_star_max = cms.double(1000),
  mightGet = cms.optional.untracked.vstring
)
