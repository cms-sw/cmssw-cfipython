import FWCore.ParameterSet.Config as cms

photonCountFilter = cms.EDFilter('PhotonCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
