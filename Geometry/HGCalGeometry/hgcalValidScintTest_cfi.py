import FWCore.ParameterSet.Config as cms

hgcalValidScintTest = cms.EDAnalyzer('HGCalValidScintTest',
  mightGet = cms.optional.untracked.vstring
)
