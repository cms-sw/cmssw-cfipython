import FWCore.ParameterSet.Config as cms

siStripExcludedFEDListProducer = cms.EDProducer('SiStripExcludedFEDListProducer',
  ProductLabel = cms.InputTag('rawDataCollector')
)
