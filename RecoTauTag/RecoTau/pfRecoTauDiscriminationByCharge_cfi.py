import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByCharge = cms.EDProducer('PFRecoTauDiscriminationByCharge',
  AbsChargeReq = cms.uint32(1),
  ApplyOneOrThreeProngCut = cms.bool(False),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  PFTauProducer = cms.InputTag('pfRecoTauProducerHighEfficiency')
)
