import FWCore.ParameterSet.Config as cms

deepCoreSeedGenerator = cms.EDProducer('DeepCoreSeedGenerator',
  vertices = cms.InputTag('offlinePrimaryVertices'),
  pixelClusters = cms.InputTag('siPixelClustersPreSplitting'),
  cores = cms.InputTag('jetsForCoreTracking'),
  ptMin = cms.double(300),
  deltaR = cms.double(0.1),
  chargeFractionMin = cms.double(18000),
  centralMIPCharge = cms.double(2),
  pixelCPE = cms.string('PixelCPEGeneric'),
  weightFile = cms.FileInPath('RecoTracker/TkSeedGenerator/data/DeepCore/DeepCoreSeedGenerator_TrainedModel_barrel_2017.pb'),
  inputTensorName = cms.vstring(
    'input_1',
    'input_2',
    'input_3'
  ),
  outputTensorName = cms.vstring(
    'output_node0',
    'output_node1'
  ),
  probThr = cms.double(0.85),
  mightGet = cms.optional.untracked.vstring
)
