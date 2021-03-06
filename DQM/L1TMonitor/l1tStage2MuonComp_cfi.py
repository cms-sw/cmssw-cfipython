import FWCore.ParameterSet.Config as cms

l1tStage2MuonComp = cms.EDProducer('L1TStage2MuonComp',
  muonCollection1 = cms.required.InputTag,
  muonCollection2 = cms.required.InputTag,
  monitorDir = cms.untracked.string(''),
  muonCollection1Title = cms.untracked.string('Muon collection 1'),
  muonCollection2Title = cms.untracked.string('Muon collection 2'),
  summaryTitle = cms.untracked.string('Summary'),
  ignoreBin = cms.untracked.vint32(),
  verbose = cms.untracked.bool(False),
  enable2DComp = cms.untracked.bool(False),
  displacedQuantities = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
