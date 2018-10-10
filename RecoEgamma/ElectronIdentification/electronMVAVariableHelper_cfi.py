import FWCore.ParameterSet.Config as cms

electronMVAVariableHelper = cms.EDProducer('ElectronMVAVariableHelper',
  conversions = cms.InputTag('allConversions'),
  src = cms.InputTag('gedGsfElectrons'),
  srcMiniAOD = cms.InputTag('slimmedElectrons', '', '@skipCurrentProcess'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  conversionsMiniAOD = cms.InputTag('reducedEgamma', 'reducedConversions'),
  vertexCollection = cms.InputTag('offlinePrimaryVertices'),
  vertexCollectionMiniAOD = cms.InputTag('offlineSlimmedPrimaryVertices')
)
