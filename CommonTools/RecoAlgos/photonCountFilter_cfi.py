import FWCore.ParameterSet.Config as cms

photonCountFilter = cms.EDFilter('PhotonCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
