import FWCore.ParameterSet.Config as cms

siStripClustersFromSOA = cms.EDProducer('SiStripClustersFromSOA',
  ProductLabel = cms.InputTag('siStripClustersSOAtoHost'),
  mightGet = cms.optional.untracked.vstring
)
