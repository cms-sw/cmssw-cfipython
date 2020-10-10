import FWCore.ParameterSet.Config as cms

ctppsLHCInfoPlotter = cms.EDAnalyzer('CTPPSLHCInfoPlotter',
  lhcInfoLabel = cms.string(''),
  outputFile = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
