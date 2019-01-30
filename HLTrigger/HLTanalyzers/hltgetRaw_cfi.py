import FWCore.ParameterSet.Config as cms

hltgetRaw = cms.EDAnalyzer('HLTGetRaw',
  RawDataCollection = cms.InputTag('rawDataCollector')
)
