import FWCore.ParameterSet.Config as cms

PackedPFTowers = cms.EDProducer('PackedPFTowers',
  useHF = cms.bool(True),
  src = cms.InputTag('packedPFCandidates'),
  mightGet = cms.optional.untracked.vstring
)
