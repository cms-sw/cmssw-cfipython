import FWCore.ParameterSet.Config as cms

particleFlowEGamma = cms.EDProducer('PFEGammaProducer',
  useVerticesForNeutral = cms.bool(True),
  produceEGCandsWithNoSuperCluster = cms.bool(False),
  pf_electron_mvaCut = cms.double(-0.1),
  pf_electronID_crackCorrection = cms.bool(False),
  pf_conv_mvaCut = cms.double(0),
  blocks = cms.InputTag('particleFlowBlock'),
  EEtoPS_source = cms.InputTag('particleFlowClusterECAL'),
  vertexCollection = cms.InputTag('offlinePrimaryVertices'),
  pf_electronID_mvaWeightFile = cms.FileInPath('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt'),
  pf_convID_mvaWeightFile = cms.FileInPath('RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt')
)
