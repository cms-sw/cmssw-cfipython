import FWCore.ParameterSet.Config as cms

etMinPhotonCountFilter = cms.EDFilter('EtMinPhotonCountFilter',
  src = cms.InputTag(''),
  etMin = cms.double(0),
  minNumber = cms.uint32(0)
)
