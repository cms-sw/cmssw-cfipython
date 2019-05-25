import FWCore.ParameterSet.Config as cms

muonGEMDigisDefault = cms.EDProducer('GEMRawToDigiModule',
  InputLabel = cms.InputTag('rawDataCollector'),
  useDBEMap = cms.bool(False),
  unPackStatusDigis = cms.bool(False)
)
