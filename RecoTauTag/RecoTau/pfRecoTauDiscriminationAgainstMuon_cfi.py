import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstMuon = cms.EDProducer('PFRecoTauDiscriminationAgainstMuon',
  a = cms.double(0.5),
  c = cms.double(0),
  b = cms.double(0.5),
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  discriminatorOption = cms.string('noSegMatch'),
  HoPMin = cms.double(0.2),
  maxNumberOfMatches = cms.int32(0),
  checkNumMatches = cms.bool(False)
)
