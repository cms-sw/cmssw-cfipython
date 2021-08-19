import FWCore.ParameterSet.Config as cms

muonGEMDigisDefault = cms.EDProducer('GEMRawToDigiModule',
  InputLabel = cms.InputTag('rawDataCollector'),
  useDBEMap = cms.bool(False),
  keepDAQStatus = cms.bool(False),
  readMultiBX = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
