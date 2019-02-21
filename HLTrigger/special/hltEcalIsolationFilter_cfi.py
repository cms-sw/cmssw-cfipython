import FWCore.ParameterSet.Config as cms

hltEcalIsolationFilter = cms.EDFilter('HLTEcalIsolationFilter',
  saveTags = cms.bool(True),
  EcalIsolatedParticleSource = cms.InputTag('ecalIsolPartProd'),
  MaxNhitInnerCone = cms.int32(1000),
  MaxNhitOuterCone = cms.int32(0),
  MaxEnergyOuterCone = cms.double(10000),
  MaxEnergyInnerCone = cms.double(10000),
  MaxEtaCandidate = cms.double(1.3)
)
