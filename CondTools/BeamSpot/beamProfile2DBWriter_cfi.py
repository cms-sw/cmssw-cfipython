import FWCore.ParameterSet.Config as cms

beamProfile2DBWriter = cms.EDAnalyzer('BeamProfile2DBWriter',
  X0 = cms.required.double,
  Y0 = cms.required.double,
  Z0 = cms.required.double,
  SigmaZ = cms.required.double,
  BetaStar = cms.required.double,
  Emittance = cms.required.double,
  Alpha = cms.double(0),
  Phi = cms.double(0),
  TimeOffset = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
