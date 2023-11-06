import FWCore.ParameterSet.Config as cms

siStripClustersSOAtoHost = cms.EDProducer('SiStripClustersSOAtoHost',
  ProductLabel = cms.InputTag('siStripClusterizerFromRawGPU'),
  mightGet = cms.optional.untracked.vstring
)
