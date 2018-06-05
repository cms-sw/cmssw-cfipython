import FWCore.ParameterSet.Config as cms

cosmicRateAnalyzer = cms.EDAnalyzer('CosmicRateAnalyzer',
  tracksInputTag = cms.InputTag('ALCARECOTkAlCosmicsCTF0T'),
  muonsInputTag = cms.InputTag('muons1Leg')
)
