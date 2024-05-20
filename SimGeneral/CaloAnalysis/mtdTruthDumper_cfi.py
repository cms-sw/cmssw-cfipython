import FWCore.ParameterSet.Config as cms

mtdTruthDumper = cms.EDAnalyzer('MtdTruthDumper',
  moduleLabelMtdSimLC = cms.InputTag('mix', 'MergedMtdTruthLC'),
  mightGet = cms.optional.untracked.vstring
)
