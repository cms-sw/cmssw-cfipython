import FWCore.ParameterSet.Config as cms

etMinSuperClusterCountFilter = cms.EDFilter('EtMinSuperClusterCountFilter',
  src = cms.InputTag(''),
  etMin = cms.double(0),
  minNumber = cms.uint32(0)
)
