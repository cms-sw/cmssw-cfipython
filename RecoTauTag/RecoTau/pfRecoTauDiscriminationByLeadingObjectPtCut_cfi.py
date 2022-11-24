import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByLeadingObjectPtCut = cms.EDProducer('PFRecoTauDiscriminationByLeadingObjectPtCut',
  MinPtLeadingObject = cms.double(5),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  UseOnlyChargedHadrons = cms.bool(False),
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  mightGet = cms.optional.untracked.vstring
)
