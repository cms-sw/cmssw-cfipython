import FWCore.ParameterSet.Config as cms

hgCalMappingESSourceTester = cms.EDAnalyzer('HGCalMappingESSourceTester',
  mightGet = cms.optional.untracked.vstring
)
