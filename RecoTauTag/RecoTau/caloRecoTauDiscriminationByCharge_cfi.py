import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByCharge = cms.EDProducer('CaloRecoTauDiscriminationByCharge',
  AbsChargeReq = cms.uint32(1),
  ApplyOneOrThreeProngCut = cms.bool(False),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  CaloTauProducer = cms.InputTag('caloRecoTauProducerHighEfficiency')
)
