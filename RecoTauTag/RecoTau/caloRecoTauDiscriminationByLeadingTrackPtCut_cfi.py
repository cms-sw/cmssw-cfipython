import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationByLeadingTrackPtCut = cms.EDProducer('CaloRecoTauDiscriminationByLeadingTrackPtCut',
  MinPtLeadingTrack = cms.double(5),
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  )
)
