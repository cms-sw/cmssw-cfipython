import FWCore.ParameterSet.Config as cms

simAnalyzerMinbias = cms.EDAnalyzer('SimAnalyzerMinbias',
  TimeCut = cms.untracked.double(500),
  mightGet = cms.optional.untracked.vstring
)
