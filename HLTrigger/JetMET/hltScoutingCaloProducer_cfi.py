import FWCore.ParameterSet.Config as cms

hltScoutingCaloProducer = cms.EDProducer('HLTScoutingCaloProducer',
  caloJetCollection = cms.InputTag('hltAK4CaloJets'),
  vertexCollection = cms.InputTag('hltPixelVertices'),
  metCollection = cms.InputTag('hltMet'),
  rho = cms.InputTag('hltFixedGridRhoFastjetAllCalo'),
  caloJetPtCut = cms.double(20),
  caloJetEtaCut = cms.double(3),
  doMet = cms.bool(True)
)
