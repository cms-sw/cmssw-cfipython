import FWCore.ParameterSet.Config as cms

ecalScaleFactorCalculator = cms.EDAnalyzer('TreeWriterForEcalCorrection',
  mightGet = cms.optional.untracked.vstring
)
