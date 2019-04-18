import FWCore.ParameterSet.Config as cms

hltMuonPointingFilter = cms.EDFilter('HLTMuonPointingFilter',
  SALabel = cms.InputTag('hltCosmicMuonBarrelOnly'),
  PropagatorName = cms.string('SteppingHelixPropagatorAny'),
  radius = cms.double(90),
  maxZ = cms.double(280)
)
