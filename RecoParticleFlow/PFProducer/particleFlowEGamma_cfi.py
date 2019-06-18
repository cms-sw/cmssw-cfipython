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
  pf_electronID_mvaWeightFile = cms.FileInPath('RecoParticleFlow/PFProducer/data/PfElectrons23Jan_BDT.weights.xml.gz'),
  pf_convID_mvaWeightFile = cms.FileInPath('RecoParticleFlow/PFProducer/data/pfConversionAug0411_BDT.weights.xml.gz'),
  mightGet = cms.optional.untracked.vstring
)
