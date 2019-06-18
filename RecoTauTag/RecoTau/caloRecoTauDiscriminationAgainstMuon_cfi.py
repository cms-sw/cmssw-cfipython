import FWCore.ParameterSet.Config as cms

caloRecoTauDiscriminationAgainstMuon = cms.EDProducer('CaloRecoTauDiscriminationAgainstMuon',
  CaloTauProducer = cms.InputTag('caloRecoTauProducer'),
  muonSource = cms.InputTag('muons'),
  muonCompCut = cms.double(0),
  segmCompCoefficient = cms.double(0.5),
  dRmatch = cms.double(0.5),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  discriminatorOption = cms.string('noSegMatch'),
  caloCompCoefficient = cms.double(0.5),
  mightGet = cms.optional.untracked.vstring
)
