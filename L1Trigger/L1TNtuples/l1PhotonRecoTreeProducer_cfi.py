import FWCore.ParameterSet.Config as cms

l1PhotonRecoTreeProducer = cms.EDAnalyzer('L1PhotonRecoTreeProducer',
  maxPhoton = cms.uint32(20),
  mightGet = cms.optional.untracked.vstring
)