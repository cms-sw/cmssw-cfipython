import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationAgainstMuonMVA = cms.EDProducer('PFRecoTauDiscriminationAgainstMuonMVA',
  mvaMin = cms.double(0),
  mvaName = cms.string('againstMuonMVA'),
  PFTauProducer = cms.InputTag('pfTauProducer'),
  verbosity = cms.int32(0),
  returnMVA = cms.bool(True),
  inputFileName = cms.FileInPath('RecoTauTag/RecoTau/data/emptyMVAinputFile'),
  loadMVAfromDB = cms.bool(True),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet()
  ),
  dRmuonMatch = cms.double(0.3),
  srcMuons = cms.InputTag('muons')
)
