import FWCore.ParameterSet.Config as cms

l1tStage2MuonShowerComp = cms.EDProducer('L1TStage2MuonShowerComp',
  muonShowerCollection1 = cms.required.InputTag,
  muonShowerCollection2 = cms.required.InputTag,
  monitorDir = cms.untracked.string(''),
  muonShowerCollection1Title = cms.untracked.string('Muon Shower collection 1'),
  muonShowerCollection2Title = cms.untracked.string('Muon Shower collection 2'),
  summaryTitle = cms.untracked.string('Summary'),
  ignoreBin = cms.untracked.vint32(),
  verbose = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
